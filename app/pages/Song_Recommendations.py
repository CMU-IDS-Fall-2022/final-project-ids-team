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

st.markdown("# Song Recommendations")