import streamlit as st
from PIL import Image
import io
import requests
import time

def get_prediction(picture):
    t=time.time()
    image_bytes = picture.getvalue()
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('RGB')

    st.image(image, caption='Uploaded Image',use_column_width=True)
    with st.spinner("Predicting Image..."):
        # response = requests.post("https://fast-api-backend-nzhkc6v44a-du.a.run.app/inference", files={'files': picture})
        response = requests.post("http://0.0.0.0:8000/inference", files={'files': picture})
        label = response.json()[0]
        percent = response.json()[1]
    st.metric("Type",label)
    st.metric("Time Taken",f"{time.time()-t:.3f} sec")
    st.metric("Prediction Score", f"{percent}%")

def get_prediction_sashimi(picture):
    t=time.time()
    image_bytes = picture.getvalue()
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('RGB')

    st.image(image, caption='Uploaded Image',use_column_width=True)
    with st.spinner("Predicting Image..."):
        # response = requests.post("https://fast-api-backend-nzhkc6v44a-du.a.run.app/inference_sashimi", files={'files': picture})
        response = requests.post("http://0.0.0.0:8000/inference_sashimi", files={'files': picture})
        label = response.json()[0]
        percent = response.json()[1]
    st.metric("Type",label)
    st.metric("Time Taken",f"{time.time()-t:.3f} sec")
    st.metric("Prediction Score", f"{percent}%")

def start():
    # return requests.get("https://fast-api-backend-nzhkc6v44a-du.a.run.app/blob_name").json()
    return requests.get("http://0.0.0.0:8000/blob_name").json()

def start_sashimi():
    # return requests.get("https://fast-api-backend-nzhkc6v44a-du.a.run.app/blob_name").json()
    return requests.get("http://0.0.0.0:8000/blob_name_sashimi").json()

name=start()
st.title("FICV")
st.markdown(f"<h6 style='text-align: right; color: grey'> {name} </h6>",unsafe_allow_html=True)

genre_sashimi = st.radio(
    "Image Mode:",
    ('Upload', 'Camera'),key=1)

if genre_sashimi == 'Upload':
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg","png"], key=2)
    if uploaded_file:
        get_prediction(uploaded_file)
else:
    picture = st.camera_input("Take a picture", key=3)
    if picture:
        get_prediction(picture)
        
name_sashimi=start_sashimi()    
st.markdown(f"<h6 style='text-align: right; color: grey'> {name_sashimi} </h6>",unsafe_allow_html=True)      
genre_sashimi = st.radio(
    "Image Mode:",
    ('Upload', 'Camera'), key=4)

if genre_sashimi == 'Upload':
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg","png"], key=5)
    if uploaded_file:
        get_prediction_sashimi(uploaded_file)
else:
    picture = st.camera_input("Take a picture", key=6)
    if picture:
        get_prediction_sashimi(picture)

st.markdown(f"<h6 style='text-align: right; color: grey'> We collect your data to ensure you have the best browsing experience on our website. </h6>",unsafe_allow_html=True)
st.markdown(f"<h6 style='text-align: right; color: grey'> By using our site, you acknowledge that you have read and understood our Privacy Policy. </h6>",unsafe_allow_html=True)
