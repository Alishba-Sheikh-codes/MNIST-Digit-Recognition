import streamlit as st
from PIL import Image, ImageOps
import numpy as np

# Optional: Load trained model from file
import joblib
rf = joblib.load("random_forest_model.pkl")

st.set_page_config(page_title="Digit Classifier", layout="centered")
st.title("🧠 MNIST Digit Classifier (Random Forest)")
st.write("Draw a digit OR upload an image. The model will predict the digit (0–9).")

# === 2. Image Upload ===
st.subheader("📤 Upload a Digit Image")
uploaded_file = st.file_uploader("Choose an image file...", type=["png", "jpg", "jpeg"])

image = None

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=False)
# === 3. Prediction ===
if image is not None:
    # Ensure image is in grayscale (L mode)
    image = image.convert("L")

    # Preprocess: resize and invert
    img_resized = ImageOps.invert(image).resize((28, 28))
    arr = np.array(img_resized).reshape(1, -1)

    if "rf" in globals():
        prediction = rf.predict(arr)[0]
        st.success(f"✅ Predicted Digit: {prediction}")
    else:
        st.error("❌ Random Forest model (`rf`) is not loaded. Please define or load it.")