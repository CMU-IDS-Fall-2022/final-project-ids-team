import streamlit as st
from PIL import Image

image1 = Image.open('sunrise.jpg')
image2 = Image.open('sunrise.jpg')

page_bg = """
    <style>
    [data-testid="stSidebar"]{
        background-color: black;
    }
    [data-testid="stSidebar"] span{
        color: white;
    }
    </style>
"""
st.markdown(page_bg, unsafe_allow_html = True)

st.markdown("# Billboard Top 50 Songs Data Analysis using Spotify Data!")
st.image([image1,image2])


st.markdown("Add motivation and describe the pages here")
#TODO: writeup, intro to page
#TODO: brief description of all the musical features