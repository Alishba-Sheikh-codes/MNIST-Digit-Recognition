#  MNIST Digit Classifier (Random Forest)

This is a simple Streamlit web app that classifies handwritten digits (0–9) using a pre-trained Random Forest model. Users can upload digit images (e.g., PNG or JPG files), and the app predicts the digit shown in the image.

---

## 📂 Project Structure

📁MNIST/
├── app.py # Streamlit application script
├── random_forest_model.pkl # Trained Random Forest model (will be formed when you run random classifier cell)
|── nine.png
│── two.jpg #images for testing in streamlit app
│── ...
└── README.md # This file

## 📸 Sample Predictions

| Input Image | Predicted Digit |
|-------------|-----------------|
| ![nine](MNIST-Digit-Recognition/nine.png) | 9 |
| ![two](MNIST-Digit-Recognition/two.jpg) | 2 |
## ⚙️ How to Run the App (Anaconda Prompt)

1. Open **Anaconda Prompt**.
2. Navigate to your project directory:
   cd path\to\your_working_directory
Run the Streamlit app:
streamlit run app.py
A browser window will open with the web interface.

🧪 Model Details
Algorithm: Random Forest Classifier
Note: when running random classifier model cell, a file name random_forest_model.pkl will be formed in the same working directory, couldn't upload it here as the size of the file was large.

Training Data: MNIST digit dataset

Input: Uploaded grayscale digit images

Preprocessing:

Grayscale conversion

Inversion (white digit on black background)

Resize to 28x28 pixels

Output: Predicted digit label (0–9)

🏁 License
This project is open-source and free to use for educational purposes.
