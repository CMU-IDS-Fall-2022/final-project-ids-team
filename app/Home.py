import streamlit as st

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

st.markdown("# Spotify Data Analysis!")

st.markdown("Add motivation and describe the pages here")
#TODO: writeup, intro to page
#TODO: brief description of all the musical features