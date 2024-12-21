from fastai.vision.all import *
import streamlit as st
import pathlib
import plotly.express as px

# title
st.title('Banan,lemon va olmaning klassifikatsiya qiluvchi model')

# rasmni joylash
file = st.file_uploader('Rasm yuklash', type=['png', 'jpeg', 'gif', 'svg'])

if file:
    st.image(file)
    # Convert the uploaded image to PILImage
    img = PILImage.create(file)
    
    # Model loading
    model = load_learner('/Users/aaaa/Downloads/Fruit/venv/etc/Fruit.pkl')
    
    # Prediction
    pred, pred_id, probs = model.predict(img)
    
    # Show prediction results
    st.success(f"Bashorat: {pred}")
    st.info(f'Ehtimollik: {probs[pred_id] * 100: 1f}%')
