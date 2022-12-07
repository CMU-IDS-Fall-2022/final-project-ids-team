import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

#  div[class="st-au st-av st-aw st-ax st-ba st-bc st-b6 st-b3 st-b4 st-bd st-be st-bf st-bg st-bh st-bi st-bj st-bk st-bl st-bm st-b1 st-bn st-bo st-bp st-bq st-br st-bs st-bt"] {
#         border-block-color: green;
#         border-color: green;
#     }
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

feats = ['BPM','Energy','Danceability','Loudness','Liveness','Valence','Duration','Acousticness','Speechiness','Popularity']
@st.cache  # add caching so we load the data only once
def load_data(md):
    df = pd.read_csv('data/cleaned.csv', encoding='latin-1').groupby("Year").agg(md)
    return df


#TODO: modify x-axis so every year shows up and not like 2,014

st.markdown("# Change Over Time")

st.markdown("#### In this page we explore how the characteristics of popular songs changed over the years.")

agg_mode = st.selectbox('We present aggregations of the Spotify features. Choose how you wish to aggregate:', 
['mean', 'min', 'max', 'median']) 

with st.spinner(text="Loading data..."):
    df = load_data(agg_mode)


##### Plot 2 ##########
st.markdown("Heatmap of the aggregated data, with feature values normalised to a (0,1) range.")
#source: https://stackoverflow.com/questions/65871604/how-to-display-heatmap-color-correlation-plot-in-streamlit
fig, ax = plt.subplots()
#source: https://www.educative.io/answers/how-to-normalize-all-columns-in-a-dataframe-in-pandas
normalised_df = df[feats].apply(lambda iterator: ((iterator - iterator.min())/(iterator.max() - iterator.min())).round(2))
sns.heatmap(normalised_df.T, ax=ax, cmap="Greens")
st.write(fig)


############ PLOT 1 #######################
st.markdown("Raw features plotted on the line plot")
p1_selected_features = st.multiselect('Choose features to visualise', feats)
print(p1_selected_features)

if p1_selected_features == []:
    p1_selected_features = feats

print(p1_selected_features)

#source: https://github.com/altair-viz/altair/issues/968
data = df[p1_selected_features].reset_index().melt('Year')

p1_chart = alt.Chart(data).mark_line().encode(
    x='Year',
    y='value',
    color='variable'
).properties(width=600, height=250).interactive()
st.altair_chart(p1_chart)

