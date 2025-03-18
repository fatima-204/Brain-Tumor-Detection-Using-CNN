# Brain Tumor Detection Using CNN

This repository contains a deep learning project for detecting and classifying brain tumors from MRI scans using Convolutional Neural Networks (CNNs). The model classifies tumors into **4 categories** (e.g., Glioma, Meningioma, Pituitary, No Tumor) and is deployed using **Gradio** for easy interaction.

## Features

- **CNN Model**: Built using TensorFlow/Keras for accurate classification.
- **4-Class Classification**: Classifies MRI scans into Glioma, Meningioma, Pituitary, or No Tumor.
- **Gradio Deployment**: Interactive web interface for easy model testing.
- **Preprocessing**: Includes scripts for preprocessing MRI scans.

## Usage

1. Clone the repository:
  

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional):
  
4. Run the Gradio app:
   ```bash
   python app.py
   ```

5. Open the Gradio interface in your browser and upload an MRI scan for classification.

## Requirements

- Python 3.x
- TensorFlow 2.x
- Gradio
- NumPy
- OpenCV
- Matplotlib

Example `requirements.txt`:
```plaintext
tensorflow>=2.0.0
gradio>=2.0.0
numpy>=1.19.0
opencv-python>=4.5.0
matplotlib>=3.3.0
```

## Model Details

- **CNN Architecture**: Custom CNN model trained on MRI scan datasets.
- **4-Class Classification**: Classifies MRI scans into:
  1. Glioma
  2. Meningioma
  3. Pituitary
  4. No Tumor
- **Gradio Interface**: Simple and interactive UI for testing the model.

## Example

1. Run the Gradio app:
   ```bash
   python app.py
   ```

2. Upload an MRI scan through the Gradio interface.

3. View the predicted tumor class:
   ```
   Predicted Class: Pituitary
   ```

