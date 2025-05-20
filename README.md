# Cats vs. Dogs: Image Classification with CNN

A deep learning project for binary image classification using a convolutional neural network (CNN) to distinguish between images of cats and dogs. Developed as part of the coursework for CSCI 3344: Artificial Intelligence at Trinity University.

## Collaborators
This project is a collaboration between Jose Salazar, Lilian Padilla, Stella Miliatis, and William Wallace


## Overview

This project uses a convolutional neural network built in Keras to automatically extract and learn visual features from images. It classifies images into two categories: **cat** or **dog**, using the [Kaggle Dogs vs. Cats dataset](https://kaggle.com/competitions/dogs-vs-cats).

Key tasks included:
- Dataset preprocessing and augmentation
- Building and evaluating multiple CNN architectures
- Hyperparameter tuning (filters, batch size, epochs)
- Analysis of overfitting, underfitting, and model depth

The final model achieved **91.20% test accuracy**.


## Technologies Used

- Python 3
- Keras (TensorFlow backend)
- NumPy, Matplotlib
- Kaggle Dataset: [Dogs vs. Cats](https://kaggle.com/competitions/dogs-vs-cats)

## CNN Architecture

### Final Model Summary:
- Input shape: `150x150x3` (RGB)
- **3 Convolutional + MaxPooling layers**
  - Filters: 24 → 48 → 96
  - Filter size: `3x3`, Pooling: `2x2`, Stride: `2`
- **Image Augmentation**:
  - Horizontal flip
  - Shifting (up to 10%)
  - Rotation (up to 30°)
  - Shearing/skewing (up to 20%)
- **Fully Connected Layers**:
  - Dense(64), ReLU
  - Dense(1), Sigmoid (for binary classification)

---

## Results

| Trial | Change                             | Accuracy (%) |
|-------|-------------------------------------|--------------|
| 10    | Baseline (2-layer) CNN              | ~79%         |
| 15    | Added 3rd Conv layer (128 filters)  | +3.5%        |
| 17    | Reduced filters (24/48/96)          | +2.1%        |
| 24    | Added data augmentation             | ~85%         |
| 34    | +25 epochs, final model             | **91.20%**   |

---

## Limitations

- Dataset contained mislabeled, irrelevant, or low-quality images
- Some images did not feature a single, centered pet subject
- Hardware constraints (personal laptops) limited training time and model depth
- Batch normalization did not improve performance as expected

---

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/lilianpadilla/CatsVsDogs.git
   cd CatsVsDogs
   ```
2. **Environment Setup**:
   
      This project requires the following libraries:
  
  - `matplotlib` 3.0.2  
  - `Keras` 2.2.4  
  - `NumPy` 1.15.2  
  - `piexif` 1.1.2  
  
     All required dependencies and versions are listed in the `environment.yml` file included in this repository.
  
    To create the environment using Conda:
    ```bash
    conda env create -f environment.yml
    ```
    Once the environment is created, you can enter it by runnning the following command:
    ```bash
    conda activate project3
    ```

3. **Running Model**:
   
   To run a model:
    ```bash
    python main_basic_cnn.py #or other model
    ```

