import streamlit as st
import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load your trained face mask detection model
model = tf.keras.models.load_model('mask_detection.h5')

# Define labels for face mask classes
labels = ['Mask Worn Wrongly', 'No Mask', 'Face Mask On']

# Create a Streamlit app
st.title('Face Mask Detection App')

# Allow the user to upload an image
uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    image = load_img(uploaded_image, target_size=(180, 180))  # Resize the uploaded image
    image = img_to_array(image)
    image = image / 255.0  # Normalize the image

    image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Use the model to make predictions
    prediction = model.predict(image)
    class_index = np.argmax(prediction)
    confidence = prediction[0][class_index]

    # Display the prediction
    st.success(f'Prediction: {labels[class_index]} with confidence {confidence:.2f}')
