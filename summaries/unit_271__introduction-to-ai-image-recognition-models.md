---
title: "Introduction to AI Image Recognition Models"
unit_id: 271
course_id: 0
level: "Foundation"
slug: introduction-to-ai-image-recognition-models
is_course: 0
---

# Introduction to AI Image Recognition Models

Tutorial on AI image recognition using Walhtinez and Walhtinez (2024) modeling framework (https://doi.org/10.1111/2041-210X.14278). Jupyter Notebook: https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Introduction%20to%20AI%20Image%20Recognition%20Models.ipynb.

Python libraries: concurrent.futures (parallel processing), functools, math, pathlib, tempfile, typing (Iterator, List, Tuple), absl (logging), google.cloud.storage (GCS), numpy, tensorflow (TensorFlow machine learning library).

Image file formats supported: jpg, jpeg, gif, png (note: both jpg and jpeg suffixes required for compatibility).

Key functions:

_iter_folder_images: Iterator function; yields image files matching supported suffixes from directory.

triplet_safe_image_dataset_from_directory: Create triplet-safe TensorFlow dataset from directory structure. Parameters: path (directory), image_size (resize target, optional), shuffle (boolean), batch_size (default 32), color_mode (rgb/rgba/grayscale), seed (random state). Functionality: inspect subdirectories as classes, list images by label, read images (decode, convert grayscale if needed, resize), shuffle samples, create TensorFlow dataset from generator, set attributes (file_paths, class_names).

load_dataset: Load dataset with train/val/test splits. Parameters: path, splits (list of fractions summing to 1.0), batch_size, seed, kwargs. Workflow: create split indices, split subdirectories by fractions, write to temporary directory with symlinks, load training/validation via triplet_safe function, load test set via keras image_dataset_from_directory.

download_from_gcloud: Download images from Google Cloud Storage (GCS) bucket. Parameters: bucket_name, output_dir, prefix (blob filter), parallelism (default 32 max workers). Uses concurrent.futures.ThreadPoolExecutor for parallel downloads; creates output directory structure; handles exceptions.

Image processing: _read_image reads file, decodes image, converts to grayscale if specified, resizes to image_size, reshapes to (image_size[0], image_size[1], channels).

Dataset specifications: TensorSpec (shape, dtype) defines dataset tensor signature; batch processing for training efficiency; TensorFlow data API for scalable data loading.

## Summarized attachments
- **Introduction to AI Image Recognition Models** (github.com/jakehosen/cybertraining_ecology, notebook): Jupyter Notebook implementing AI image recognition using Walhtinez and Walhtinez (2024) framework with TensorFlow library. Covers image file handling (jpg, jpeg, gif, png formats), triplet-safe dataset creation from directory structures, train/val/test split loading, and Google Cloud Storage (GCS) integration. Includes functions for image iteration, dataset creation with batching and shuffling, grayscale/RGB conversion, image resizing, and parallel GCS downloads using ThreadPoolExecutor.
