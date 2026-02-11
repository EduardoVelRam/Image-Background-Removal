import streamlit as st
from PIL import Image
from rembg import remove
import io

# Functions
# Process the uploaded image and remove the background
def process_image(image_uploaded):
    image = Image.open(image_uploaded)
    output_image = remove_background(image)
    return output_image

# Convert the image to bytes and remove the background
def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format='PNG')
    image_byte.seek(0)
    processed_image = remove(image_byte.read())
    return Image.open(io.BytesIO(processed_image))


# Frontend
st.image("assets/cat_remove.jpg")
st.header("Background Removal App")
st.subheader("Upload an image to remove its background")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    remove_button = st.button("Remove Background")

    if remove_button:

        processed_image = process_image(uploaded_file)
        st.image(processed_image, caption="Processed Image", use_column_width=True)
        processed_image.save("output_no_bg.png")

        with open("output_no_bg.png", "rb") as f:
            image_data = f.read()
        st.download_button("Download Processed Image", data=image_data, file_name="output_no_bg.png")
        processed_image.save("result/output_no_bg.png")
