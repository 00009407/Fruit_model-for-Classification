# Fruit Classification Model

This repository contains a machine learning model for classifying fruit images using deep learning. The model is built using **fastai**, a high-level deep learning library built on top of PyTorch, and leverages transfer learning to classify fruit images accurately.

---

## Features:
- **Fruit Classification**: Identifies fruits such as bananas, apples, and lemons from image inputs.
- **Streamlit Interface**: A simple, user-friendly web interface powered by Streamlit that allows users to upload images and get real-time predictions.
- **Pre-trained Model**: The model is trained on a dataset of fruit images and can predict the type of fruit in the image with high accuracy.

---

## How to Use:
### 1. Install Dependencies  
To run this app locally, ensure you have Python 3.8+ installed. Then, install the required dependencies:
```bash
pip install fastai==2.7.18 streamlit==1.37.1
```

### 3. Run the Application:
Activate your virtual environment (if applicable) and use Streamlit to run the app:
```bash
streamlit run app.py
```

### 4. Upload an Image:
- Use the web interface to upload a fruit image (e.g., an apple or banana).
- The model will predict the fruit type along with the confidence score.

---

## Model Details:
- **Model Type**: Convolutional Neural Network (CNN) using transfer learning.
- **Framework**: Built with **fastai** and **PyTorch**.
- **Training Data**: Trained on a dataset of fruit images, including categories such as apples, bananas, and lemons.
- **Prediction Example**:  
  - Input: A fruit image (e.g., an apple).  
  - Output: The model predicts the fruit type (e.g., "Apple") with confidence (e.g., 98%).

---

## Technologies:
- **fastai**: A high-level deep learning library built on top of PyTorch.
- **Streamlit**: A framework for building interactive web applications.
- **PyTorch**: The deep learning framework used for model training.

---

## License:
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you need further adjustments!
