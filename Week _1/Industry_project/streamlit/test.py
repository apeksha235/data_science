from os import replace
import pandas as pd
from PIL import Image, ImageEnhance, ImageFilter,ImageDraw
import pdf2image 
from pytesseract import image_to_string
import pytesseract as tess
tess.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
from pdf2image import convert_from_path
import re
import streamlit as st
import requests
from io import BytesIO


def convert_pdf_to_img(pdf_file):
    try:
      return convert_from_path(pdf_file)
    except: 
     st.markdown('```Enter the path file!```')
def convert_image_to_text(file):

    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    try:
         images = convert_pdf_to_img(pdf_file)
    except: 
     st.markdown('```Enter the path file!```')
    final_text = ""

    for pg, img in enumerate(images):
        
        final_text += convert_image_to_text(img)
 
    final_text=re.sub('[\$,]', '',final_text)
    li= re.findall(r"[-+]?\d*\.\d+|\d+",final_text)
    li1=[]
    for i in li:
     if(i.isdigit()==False):
        li1.append(i)

    li2=list(map(float, li1))
    return max(li2)
response = requests.get('https://i.pinimg.com/736x/c9/96/b2/c996b223139f820547ccaa9f5c4a3891.jpg') 
logo = Image.open(BytesIO(response.content)) 
st.image(logo,width=200)
sentence = st.text_input('Enter the path of your pdf here') 
st.markdown('```This is total price is: ```')
if sentence:
    st.write(get_text_from_any_pdf(sentence))
