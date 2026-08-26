import asyncio
from dataclasses import dataclass
from typing import Iterable, List, Tuple, Any, Optional


@dataclass
class RerankResult:
    docs: List[Any]
    scores: List[float]


class RerankQueue:
    """Simple async batching queue for GPU-bound reranking with shared GPU lock.

    Usage sketch (FastAPI endpoint):
        # create once at startup (with shared gpu_lock)
        # gpu_lock = asyncio.Lock()
        # app.state.rerank_queue = RerankQueue(model, max_batch_size=16, max_wait_ms=10, gpu_lock=gpu_lock)
        # await app.state.rerank_queue.start()

        # inside endpoint
        # result = await app.state.rerank_queue.enqueue(question, docs)
        # return result.docs
    """

    def __init__(
        self,
        model,
        max_batch_size: int = 16,
        max_wait_ms: int = 10,
        min_score: Optional[float] = None,
        gpu_lock: Optional[asyncio.Lock] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self._model = model
        self._max_batch_size = max_batch_size
        self._max_wait_ms = max_wait_ms
        self._min_score = min_score
        self._gpu_lock = gpu_lock or asyncio.Lock()  # Use provided lock or create new one
        self._loop = loop or asyncio.get_event_loop()
        self._queue: asyncio.Queue[Tuple[str, List[Any], asyncio.Future]] = asyncio.Queue()
        self._worker_task: Optional[asyncio.Task] = None
        self._stop_event = asyncio.Event()

    async def start(self) -> None:
        if self._worker_task is None:
            self._worker_task = asyncio.create_task(self._worker())

    async def stop(self) -> None:
        self._stop_event.set()
        if self._worker_task is not None:
            await self._worker_task
            self._worker_task = None

    async def enqueue(self, question: str, docs: Iterable[Any]) -> RerankResult:
        if self._worker_task is None:
            raise RuntimeError("RerankQueue not started")
        future: asyncio.Future = self._loop.create_future()
        await self._queue.put((question, list(docs), future))
        return await future

    async def _worker(self) -> None:
        while not self._stop_event.is_set():
            try:
                first_item = await asyncio.wait_for(self._queue.get(), timeout=0.1)
            except asyncio.TimeoutError:
                continue

            batch = [first_item]
            start = self._loop.time()
            deadline = start + (self._max_wait_ms / 1000.0)

            # Collect up to max_batch_size within max_wait_ms.
            while len(batch) < self._max_batch_size:
                timeout = max(0.0, deadline - self._loop.time())
                if timeout == 0.0:
                    break
                try:
                    item = await asyncio.wait_for(self._queue.get(), timeout=timeout)
                    batch.append(item)
                except asyncio.TimeoutError:
                    break

            # Build a flat list of pairs for the model.
            flat_pairs: List[List[str]] = []
            spans: List[Tuple[int, int]] = []
            for question, docs, _ in batch:
                start_idx = len(flat_pairs)
                flat_pairs.extend([[question, doc.page_content] for doc in docs])
                spans.append((start_idx, len(flat_pairs)))

            # Acquire GPU lock before running the model.
            async with self._gpu_lock:
                flat_scores: List[float] = self._model.predict(flat_pairs)

            # Split results back per request.
            for (question, docs, future), (s, e) in zip(batch, spans):
                scores = flat_scores[s:e]
                ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
                if self._min_score is not None:
                    ranked = [r for r in ranked if r[0] > self._min_score]
                out_docs = [d for _, d in ranked]
                out_scores = [sc for sc, _ in ranked]
                if not future.cancelled():
                    future.set_result(RerankResult(docs=out_docs, scores=out_scores))


class RerankSemaphore:
    """Semaphore-based limiter for GPU calls.

    Usage sketch:
        # app.state.rerank_sem = RerankSemaphore(model, max_concurrent=1)
        # result = await app.state.rerank_sem.rerank(question, docs)
    """

    def __init__(self, model, max_concurrent: int = 1, min_score: Optional[float] = None) -> None:
        self._model = model
        self._sem = asyncio.Semaphore(max_concurrent)
        self._min_score = min_score

    async def rerank(self, question: str, docs: Iterable[Any]) -> RerankResult:
        async with self._sem:
            pairs = [[question, doc.page_content] for doc in docs]
            scores = self._model.predict(pairs)
            ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
            if self._min_score is not None:
                ranked = [r for r in ranked if r[0] > self._min_score]
            out_docs = [d for _, d in ranked]
            out_scores = [sc for sc, _ in ranked]
            return RerankResult(docs=out_docs, scores=out_scores)
