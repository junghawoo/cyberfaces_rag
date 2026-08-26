---
title: "Session 2: Foundations of Deep Learning: From Discriminative Models to Generative AI"
unit_id: 285
course_id: 0
slug: session-2-foundations-of-deep-learning-from-discriminative-models-to-generative-ai
is_course: 0
---

# Session 2: Foundations of Deep Learning: From Discriminative Models to Generative AI

Explores fundamental discriminative deep learning models (CNNs, RNNs, early attention mechanisms) and their transition to generative architectures. Covers feature extraction, representation learning, and autoencoders preceding the Transformer era.

**Presenter:** Dr. Elham Barezi, AI Research scientist. **Co-Sponsored:** Rosen Center for Advanced Computing (RCAC) and IPAI, Spring 2025. **Source:** deep learning series-session 2.pptx.pdf; video: RCAC_Lecture_Series____Unveiling_the_Mystery_of_Deep_Learning______Session_2_(Source).mp4.

## Deep Neural Network History and Foundations

Course covers: (1) DNN history/basics from traditional ML, AI hypes/winters, deep learning since 1950s, single neurons to deep networks, challenges solved (model overfitting, activation function saturation, vanishing/exploding gradients); (2) Fundamental models: CNN, RNN, early attention, representation learning, pre-training; (3) Discriminative vs generative: VAE, GAN, Diffusion Models; (4) Transformers, self-attention, encoders/decoders, masking; (5) LLMs: prompt engineering (COT, TOT, Self-Consistency, RAG, Agents), fine-tuning (instruct tuning, RLHF, LoRA adapters); (6) Deep learning across domains; (7) AI safety/governance.

## CNN Era (1990-2015)

**Convolutional Neural Networks** inspired by visual cortex processing. Key architectures: Neocognitron (1980, earliest CNN precursor), LeNet-5 (1998 by Yann LeCun, digit recognition on MNIST), AlexNet (2012, first ImageNet challenge winner), ResNet (2015 by Kaiming He et al., Microsoft Research, residual/skip blocks). CNN mimics visual system: LGN→preprocessing/pooling, V1→first conv layer (edge detectors), V2→second conv (shape detectors), V4→mid-conv (color/complex shapes), IT cortex→deep layers/fully connected (object representation).

**Convolution mechanics:** h(t) discrete time input, f(t) kernel function, weighted average via backpropagation and gradient descent. **CNN Elements:** filter, stride (shift amount), parameter sharing (control parameters via shared weights), padding (zero padding maintains volume size), pooling (max/average/L2-norm, downsampling, reduces parameters 75%, controls overfitting). **Key properties:** location invariance (object position irrelevant via striding), local similarity (filters extract neighborhood info), compositionality (low-level→high-level features), weight sharing (fewer parameters vs fully connected). **Challenges:** low-texture→focus on shapes (larger kernels, deeper nets), high-texture→preserve local textures (smaller kernels, more filters); CNNs don't encode relative feature positions; filters see small input portions; large filters needed for complex combinations (e.g., "eyes above nose/mouth").

## RNN and Sequential Modeling (1980s-2010s)

**Recurrent Neural Networks** process sequences (language, sound, time-series) mimicking human context influence. Parameter efficient via weight sharing across time steps, but limits position-specific behavior. **RNN cell structure:** hidden state = working memory capturing context from previous steps. Problems: hard to parallelize (sequential), slow training (autoregressive). **Solutions:** LSTM (1997, reset/forget gates, solves vanishing gradient), GRU (2014, input/output/forget gates, fewer parameters, simpler). **Attention for Machine Translation:** Bengio et al. 2015 addressed RNN limitations. RNNs applied to music/poetry generation, code generation before transformers. Still used in low-latency/resource-constrained environments.

## Representation Learning and Pre-Training

**Traditional ML relied on hand-engineered features** (TF-IDF for text, SIFT/HOG for images, Wavelet). **Deep learning enables hierarchical feature learning:** low-level (edges, 1st layers), intermediate (shapes/textures, mid-layers), high-level abstractions (objects/faces, deep layers). End-to-end learning integrates feature extraction into training; gradients flow across entire computational graph; joint optimization learns features and tasks together.

**Pre-training revolution (~2010):** Geoffrey Hinton et al. (2006), Yoshua Bengio (2007) introduced layer-wise unsupervised pretraining: each layer trained separately, stacked progressively, final supervised fine-tuning. Benefits: reduced data requirements (smaller task-specific datasets), learns broad reusable representations (grammar/syntax/semantics in NLP; edges/textures/shapes in vision; pitch/phonemes in audio), enables deeper models (stable foundation). **Stacked Autoencoders** enable unsupervised pretraining via encoder-decoder stacking.

## Discriminative vs Generative Models

**Discriminative models** learn conditional probability P(y|x): regression, SVM, RNN, CNN, BERT family. **Generative models** learn joint distribution P(x,y), use Bayes rule to deduce P(y|x): Bayes, GDA, GPT family, Diffusion models.

**Autoencoders:** compress data via encoder, reduce redundancy, but non-regularized latent space prevents valid sampling. **Variational Autoencoders (VAE, 2013):** encoder outputs latent distribution parameters; ELBO (evidence lower bound) transforms intractable inference to optimization via gradient methods. KL divergence measures additional info required for posterior vs prior; high KL = significant model learning, approaching zero = prior coverage. VAE suffers blurry generation and mode collapse (Gaussian assumption).

**Generative Adversarial Networks (GAN, 2014):** generator creates realistic content, discriminator detects fakes; competitive training. Challenges: mode collapse (limited repetitive outputs), optimization difficulty, no explicit control over samples.

**Diffusion Models (DALL-E, Stable Diffusion):** forward process adds Gaussian noise over T steps (variance schedule β_t), gradually destroying distinguishable features until x_T≈isotropic Gaussian; reverse process slowly removes noise to generate samples via Markov chain.

## References

References include Krishna et al. 2019, Nie et al. 2019, Rocca 2021 (VAEs), Raffel et al. 2020 (T5), Wang et al. 2024 (model compression), plus links to Stanford deep learning, TowardsAI, Towards Data Science, CalvinY Luo diffusion tutorial, Jeremy Jordan VAE guide.

## Summarized attachments
- **Deep learning series-session 2** (deep learning series-session 2.pptx.pdf, file): Presentation by Dr. Elham Barezi covering DNN history from AI winters and 1950s origins, CNN/RNN/attention mechanisms (LeNet-5, AlexNet, ResNet, LSTM, GRU, attention for translation), pretraining and representation learning with stacked autoencoders, discriminative vs generative models (VAE, GAN, Diffusion Models), diffusion forward/reverse processes, and their role in modern generative AI before Transformers era.
- **Non-text files (not extracted) - RCAC_Lecture_Series____Unveiling_the_Mystery_of_Deep_Learning______Session_2_(Source).mp4** (RCAC_Lecture_Series____Unveiling_the_Mystery_of_Deep_Learning______Session_2_(Source).mp4, video): Video recording of deep learning foundations lecture covering CNN development history, RNN architectures and vanishing gradients, attention mechanisms for sequence-to-sequence tasks, pretraining revolution and unsupervised layer-wise training, autoencoders for data compression, and generative models (VAE, GAN, Diffusion) foundational to modern deep learning.
