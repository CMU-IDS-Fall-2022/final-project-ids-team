import streamlit as st
from PIL import Image
import requests
from io import BytesIO

response = requests.get("https://github.com/CMU-IDS-Fall-2022/final-project-ids-team/blob/main/app/data/logos.png?raw=true")
image1 = Image.open(BytesIO(response.content))
# image1 = Image.open('./data/billboard.jpg')
# response = requests.get("https://github.com/CMU-IDS-Fall-2022/final-project-ids-team/blob/main/app/data/billboard.jpg?raw=true")
# image2 = Image.open(BytesIO(response.content))
# # image2 = Image.open('https://github.com/CMU-IDS-Fall-2022/final-project-ids-team/blob/main/app/data/spotify.png?raw=true')

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

st.markdown("# Analysis of Billboard Top Songs from 2010 to 2019 using Spotify Data!")
st.image(image1, width=800)


st.markdown("##### In this project we look at a dataset of the Top 50 Billboard songs from the years 2010 to 2019 and use \
    Spotify's musical features to perform analysis. In particular, we look to answer three overarching questions:")

st.markdown("1. Overall Popularity Analysis: What makes these songs popular?")
st.markdown("2. Trends in Popular Songs: How has popularity changed over time?")
st.markdown("3. Song Recommendations: Can we recommend similar songs from a given input?")
#TODO: writeup, intro to page
#TODO: brief description of all the musical features