import streamlit as st
import pandas as pd
import altair as alt

page_bg = """
    <style>
    [data-testid="stSidebar"]{
        background-color: black;
    }
    [data-testid="stSidebar"] span{
        color: white;
    }
    span[data-baseweb="tag"] {
    background-color: green !important;
    }
    </style>
"""
st.markdown(page_bg, unsafe_allow_html = True)

@st.cache  # add caching so we load the data only once
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/CMU-IDS-Fall-2022/final-project-ids-team/main/app/data/cleaned.csv?token=GHSAT0AAAAAABYIOQG7Z42FYYNOVKILQAQGY4SJDGQ', encoding='latin-1')
    return df

@st.cache
def get_slice_data(df, genres, years):
    labels = pd.Series([1] * len(df), index=df.index)

    if genres:
        labels &= df['Top Genre'].isin(genres)
    
    if years:
        labels &= df['Year'].isin(years)


    return labels

with st.spinner(text="Loading data..."):
    df = load_data()


st.markdown("# What makes these songs popular?")

selected_years = st.multiselect('Select a subset of years, \
    or leave unselected to consider all years.', df['Year'].unique()
    )
st.markdown("#### We now explore the overall characteristics of the selected years")


############ PLOT 1 #######################
st.markdown("Bar chart to visualise genre")


p1_labels = get_slice_data(df, None, selected_years)
print(p1_labels)

p1_chart = alt.Chart(df[p1_labels!=0]).mark_bar().encode(
    x=alt.X('count()'),
    y=alt.Y('Top Genre', sort = 'x', axis=alt.Axis(title='Genre')),
    color= alt.value('green')
).interactive() #TODO add tooltips to get values on hovering

st.altair_chart(p1_chart)

############ PLOT 2 #######################

st.markdown("Bar chart to visualise other features")

p2_selected_feature = st.selectbox('Choose a feature to visualise', 
['BPM','Energy','Danceability','Loudness','Liveness','Valence','Duration','Acousticness','Speechiness','Popularity'])
p2_labels = get_slice_data(df, None, selected_years)


p2_chart = alt.Chart(df[p2_labels!=0]).mark_bar().encode(
    x=alt.X(p2_selected_feature, bin=alt.Bin(maxbins=40)),
    y='count()',
     color= alt.value('green')
)

st.altair_chart(p2_chart)

# TODO: a plot in which we show the individual points themselves, maybe a scatterplot
# TODO: display artists 

# ############ PLOT 2 #######################

# st.markdown("Scatter plot to visualise two features on any two axes")

# p3_selected_genres = st.multiselect('Genre', df['Top Genre'].unique())
