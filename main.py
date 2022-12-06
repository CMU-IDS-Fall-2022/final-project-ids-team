import streamlit as st
import pandas as pd
import altair as alt
import requests
import json
import numpy as np
import pandas as pd
from numpy.random import normal
import plotly.express as px


st.title("Let's analyze some heat songs.")

@st.cache  # add caching so we load the data only once
def load_data():
    df = pd.read_csv('Spotify-2000.csv')
    return df

@st.cache
def get_slice_data(df, genre):
    if genre != 'others':
        labels = df['Top Genre']==genre
        return labels
    
    labels = ~df['Top Genre'].isin(['album rock', 'adult standards', 'dutch pop', 'alternative rock',
       'dance pop'])
    return labels

st.write("Please select your interested genre and observe the trend of some features from 60s to the recent.")

df = load_data()


with st.sidebar:
    st.header('Spotify Music Analysis')

# cols=st.columns(2)

# with cols[0]:
    selections = np.array(['album rock', 'adult standards', 'dutch pop', 'alternative rock',
       'dance pop', 'others'])
    genre=st.selectbox('Top Genre',selections)
# with cols[1]:
    selections = np.array(['Danceability', 'Loudness (dB)',
       'Liveness', 'Valence', 'Length (Duration)', 'Acousticness',
       'Speechiness', 'Popularity'])
    feature = st.selectbox('Feature', selections)

df_genre = df[get_slice_data(df, genre)]
d60s = df_genre[(df_genre['Year']>=1959) & (df_genre['Year']<1969)][feature].reset_index(drop=True)
d70s = df_genre[(df_genre['Year']>=1969) & (df_genre['Year']<1979)][feature].reset_index(drop=True)
d80s = df_genre[(df_genre['Year']>=1979) & (df_genre['Year']<1989)][feature].reset_index(drop=True)
d90s = df_genre[(df_genre['Year']>=1989) & (df_genre['Year']<1999)][feature].reset_index(drop=True)
d00s = df_genre[(df_genre['Year']>=1999) & (df_genre['Year']<2009)][feature].reset_index(drop=True)
d10s = df_genre[(df_genre['Year']>=2009) & (df_genre['Year']<2019)][feature].reset_index(drop=True)

colnames = ['60s', '70s', '80s', '90s', '00s', '10s']
df_concat = pd.concat([d60s, d70s, d80s, d90s, d00s, d10s], axis=1)
df_concat.columns=colnames

st.plotly_chart(
    px.violin(
        df_concat,orientation='h',labels={'variable':genre, 'value':feature}
    ).update_traces(
        side="positive", width=5, meanline_visible=True, hoveron= "kde", hoverinfo='x'
    ).update_layout(
        hovermode="closest"
    )
)

cols=st.columns(2)

with cols[0]:
    selections = np.array(['album rock', 'adult standards', 'dutch pop', 'alternative rock',
       'dance pop', 'others'])
    genre=st.selectbox('Top Genre2',selections)
with cols[1]:
    selections = np.array(['Year','Beats Per Minute (BPM)',	'Energy',	'Danceability',	'Loudness (dB)'	,'Liveness','Valence','Length (Duration)','Acousticness','Speechiness',	'Popularity'])
    simi_feature=st.selectbox('Interested feature',selections)

df_genre = df[get_slice_data(df, genre)]
diff = df_genre[simi_feature].values - df_genre[simi_feature].values[:,None]
diff_norm = 1-((diff-diff.min())/(diff.max()-diff.min()))
diff_norm[diff_norm<0.5] = 0
np.fill_diagonal(diff_norm, 0)
diff_norm = diff_norm*100
diff_matrix = pd.concat((df_genre['Title'], pd.DataFrame(diff_norm, columns=df_genre['Title'])), axis=1)

cols=st.columns(3)
with cols[0]:
    selections = np.array(['album rock', 'adult standards', 'dutch pop', 'alternative rock',
       'dance pop', 'others'])
    genre=st.selectbox('Top Genre3',selections)
with cols[1]:
    selections = np.array(['Energy','Danceability',	'Loudness (dB)'	,'Liveness','Valence','Length (Duration)','Acousticness','Speechiness'])
    feature1=st.selectbox('feature1',selections)
with cols[2]:
    selections = np.array(['Energy','Danceability',	'Loudness (dB)'	,'Liveness','Valence','Length (Duration)','Acousticness','Speechiness'])
    feature2=st.selectbox('feature2',selections)

df_genre = df[get_slice_data(df, genre)]

fig = px.scatter(df_genre, x=feature1, y=feature2, color="Top Genre")
st.plotly_chart(fig)

st.write("Here is the recommendation network based on your selection.")

