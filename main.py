import streamlit as st
import pandas as pd
import altair as alt
import requests
import json
import numpy as np
import pandas as pd


st.title("Let's analyze some heat songs.")

# @st.cache  # add caching so we load the data only once
# def load_data():
#     # Load the penguin data from https://github.com/allisonhorst/palmerpenguins.
#     url_2022 = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?year=2001"
#     resp = requests.get(url_2022)
#     data_resp = resp.json()
#     with open('chicago_crime_2022.json', 'w')as f:
#         json.dump(data_resp, f)
#     data_22 = pd.read_json('chicago_crime_2022.json')
#     return data_22

# @st.cache
# def get_slice_membership(df, crime_type, location_type):
#     """
#     Implement a function that computes which rows of the given dataframe should
#     be part of the slice, and returns a boolean pandas Series that indicates 0
#     if the row is not part of the slice, and 1 if it is part of the slice.
    
#     In the example provided, we assume genders is a list of selected strings
#     (e.g. ['Male', 'Transgender']). We then filter the labels based on which
#     rows have a value for gender that is contained in this list. You can extend
#     this approach to the other variables based on how they are returned from
#     their respective Streamlit components.
#     """
#     labels = pd.Series([True] * len(df), index=df.index)
#     if not 'All' in crime_type: 
#         if crime_type:
#             labels &= df['primary_type'].isin(crime_type)
    
#     if not 'All' in location_type: 
#         if location_type:
#             labels &= df['location_description'].isin(location_type)
    
#     return labels

st.write("Please input your favorite artist.")

artist = st.text_input(label="your favorite singer is: ")


