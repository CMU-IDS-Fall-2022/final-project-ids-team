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
st.markdown("### Exploring overall characteristics of the selected years")


############ PLOT 1 #######################
st.markdown("##### Part 1: What song genres are popular?")


p1_labels = get_slice_data(df, None, selected_years)
# print(p1_labels)

p1_chart = alt.Chart(df[p1_labels!=0]).mark_bar().encode(
    x=alt.X('count()', axis=alt.Axis(title='Number of Songs')),
    y=alt.Y('Top Genre', sort = 'x', axis=alt.Axis(title='Genre')),
    color= alt.value('green')
).interactive() #TODO add tooltips to get values on hovering


p1_chart2 = alt.Chart(df[p1_labels!=0]).mark_arc().encode(
    theta=alt.Theta("count():Q", stack=True), 
    color=alt.Color("Top Genre:N")
).properties(width = 400, height = 200)

cols=st.columns(2)

with cols[0]:
    st.altair_chart(p1_chart)
with cols[1]:
    st.altair_chart(p1_chart2)

# base = alt.Chart(df[p1_labels!=0]).encode(
#     theta=alt.Theta("count():Q", stack=True), color=alt.Color("Top Genre:N", legend=None)
# )

# pie = base.mark_arc(outerRadius=120)
# text = base.mark_text(radius=140, size=20).encode(text="Top Genre:N")

# pie + text

############ PLOT 2 #######################

st.markdown("##### Part 2: Consider a specific feature. What values does it take in the popular songs?")

# st.markdown("Bar chart to visualise other features")

p2_selected_feature = st.selectbox('Choose a feature to visualise', 
['BPM','Energy','Danceability','Loudness','Liveness','Valence','Duration','Acousticness','Speechiness','Popularity'])
p2_labels = get_slice_data(df, None, selected_years)

# st.markdown("First, we get a general overview of the distribution of "+p2_selected_feature+" values:")

p2_chart = alt.Chart(df[p2_labels!=0]).mark_bar().encode(
    x=alt.X(p2_selected_feature, bin=alt.Bin(maxbins=40)),
    y=alt.Y('count()',  axis=alt.Axis(title='Number of Songs')),
     color= alt.value('green')
)

st.altair_chart(p2_chart)

# TODO: a plot in which we show the individual points themselves, maybe a scatterplot
# TODO: display artists 

# ############ PLOT 3 #######################

st.markdown("Now we visualise at the granularity level of artists. In the plot below, each point represents an artist. \
Size of the dot is the number of times an artist is present in the dataset. On the X-axis is average year of all the \
    songs by the artist. Y-axis is average "+p2_selected_feature)

numerics = ['int', 'float']
# df = df.select_dtypes(include=numerics)
df_muneric = df.select_dtypes(include=numerics)
df_muneric['artist'] = df['artist']
maindf = df_muneric.groupby("artist").agg("mean")
counter = df.groupby("artist").agg("count")
maindf["Number of Songs"] = counter["title"]
counter = df.groupby("artist").agg(lambda x: pd.Series.mode(x)[0])
# print(counter)
maindf["genre"] = counter["Top Genre"]

maindf = maindf.reset_index()
# print(maindf)

slider = st.slider("Move slider to filter out less popular artists (Slider value indicates number of songs by artist in the dataset)", min_value=1, max_value=max(maindf["Number of Songs"]), step=1)

p3_chart = alt.Chart(maindf[maindf["Number of Songs"] >= slider]).mark_point(filled=True, opacity=1).encode(
    alt.X('Year', scale=alt.Scale(domain=[2009, 2020])),
    alt.Y(p2_selected_feature),
    alt.Color('genre', scale=alt.Scale(domain=sorted(maindf['genre'].unique().tolist()))),
    size='Number of Songs',
    # color = 'genre',
    tooltip=['artist', 'Number of Songs']
).properties(height=400,width=480)

st.altair_chart(p3_chart)


