#  MNIST Digit Classifier (Random Forest)

This is a simple Streamlit web app that classifies handwritten digits (0–9) using a pre-trained Random Forest model. Users can upload digit images (e.g., PNG or JPG files), and the app predicts the digit shown in the image.

---

## 📂 Project Structure

📁 your_project_folder/
├── app.py # Streamlit application script
├── random_forest_model.pkl # Trained Random Forest model (joblib format)
├── example_images/ # Digit images for testing
│ ├── digit_3.png
│ ├── digit_7.jpg
│ └── ...
└── README.md # This file

## 📸 Sample Predictions

| Input Image | Predicted Digit |
|-------------|-----------------|
| ![digit_3](example_images/digit_3.png) | 3 |
| ![digit_7](example_images/digit_7.jpg) | 7 |

---

## ⚙️ How to Run the App (Anaconda Prompt)

1. Open **Anaconda Prompt**.
2. Navigate to your project directory:
   cd path\to\your_project_folder
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