import streamlit as st # to work with frontend and backend
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(input_message, input_image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input_message != "":
        response = model.generate_content([input_message, input_image])
    else:
        response = model.generate_content(input_image)

    return response.text

st.set_page_config(page_title="Generative AI based ChatBot")
st.header("WinGenie ChatBot ")
input = st.text_input("Input Prompt : ", key='input')
uploaded_file = st.file_uploader("Choose an image: ", type=['jpeg','jpg','png'])

diplay_image = ""
if uploaded_file is not None:
    diplay_image = Image.open(uploaded_file)
    st.image(diplay_image, caption="uploaded image")


submit = st.button('Submit')

if submit:
    output = get_gemini_response(input_message=input, input_image=diplay_image)
    st.subheader("Your response is : ")
    st.write(output)