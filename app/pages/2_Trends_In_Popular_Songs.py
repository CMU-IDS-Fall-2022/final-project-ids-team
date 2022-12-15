import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime

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

feats = ['Energy','Danceability','Liveness','Valence','Acousticness','Speechiness']
@st.cache  # add caching so we load the data only once
def load_data(md):
    # df = pd.read_csv('data/cleaned.csv', encoding='latin-1')
    df = pd.read_csv('https://raw.githubusercontent.com/CMU-IDS-Fall-2022/final-project-ids-team/main/app/data/cleaned.csv?token=GHSAT0AAAAAABYIOQG7Z42FYYNOVKILQAQGY4SJDGQ', encoding='latin-1')
    df_agg = df.groupby("Year").agg(md)
    return df_agg, df

def load_genres():    
    # df = pd.read_csv('data/cleaned.csv', encoding='latin-1')
    df = pd.read_csv('https://raw.githubusercontent.com/CMU-IDS-Fall-2022/final-project-ids-team/main/app/data/cleaned.csv?token=GHSAT0AAAAAABYIOQG7Z42FYYNOVKILQAQGY4SJDGQ', encoding='latin-1')
    datas = []
    for year in range(2010, 2020):
        temp_data = df[df['Year'] == year]
        numrows = len(temp_data)
        temp_data = temp_data.groupby(['Top Genre']).size().to_frame(name = 'Fraction').reset_index()
        temp_data['Fraction'] /= numrows
        temp_data["Year"] = datetime.strptime(str(year), "%Y")
        datas.append(temp_data)
    df_yearly_genre_count = pd.concat(datas).reset_index()
    # print(df_yearly_genre_count)
    return df_yearly_genre_count


#TODO: modify x-axis so every year shows up and not like 2,014

st.markdown("# How has popularity changed over time?")

st.markdown("#### In this page we explore how the characteristics of popular songs changed over the years.")

with st.spinner(text="Loading data..."):
    df_genres = load_genres()
st.markdown("##### Part 1: Was there any change in what genres are popular every year?")

p0_selection = alt.selection_multi(fields=['Top Genre'], bind='legend',init=[{'Top Genre': 'dance pop'}])
# p0_selection = "dance pop"
p0_chart = alt.Chart(df_genres).mark_area().encode(
    alt.X("Year:T", axis=alt.Axis(domain=False, format='%Y', tickSize=0)),
    alt.Y("Fraction:Q", stack="zero"),
    alt.Color('Top Genre:N', scale=alt.Scale(domain=sorted(df_genres['Top Genre'].unique().tolist()))),
    opacity=alt.condition(p0_selection, alt.value(1), alt.value(0.1))
).add_selection(
    p0_selection
).transform_filter(
    p0_selection
).properties(width=800)
st.altair_chart(p0_chart)



agg_mode = st.radio('In the following plots we present aggregations of the Spotify musical features. Choose how you wish to aggregate:', 
['mean', 'min', 'max', 'median']) 

st.markdown("##### Part 2: Was there any change in "+agg_mode+" musical feature values over the years?")

with st.spinner(text="Loading data..."):
    df, df_unagg  = load_data(agg_mode)


genre_chosen = st.radio
##### Plot 2 ##########
st.markdown("###### Visualising the aggregated data as a heatmap")
#source: https://stackoverflow.com/questions/65871604/how-to-display-heatmap-color-correlation-plot-in-streamlit
fig, ax = plt.subplots()
#source: https://www.educative.io/answers/how-to-normalize-all-columns-in-a-dataframe-in-pandas
# normalised_df = df[feats].apply(lambda iterator: ((iterator - 0)/(100 - 0 )))
sns.heatmap(df[feats].T, ax=ax, cmap="Greens")
st.write(fig)


############ PLOT 1 #######################
st.markdown("##### Part 3: Closely examining desired features")
p1_selected_features = st.multiselect('Choose features to visualise', feats)
# print(p1_selected_features)

if p1_selected_features == []:
    p1_selected_features = feats

# print(p1_selected_features)

#source: https://github.com/altair-viz/altair/issues/968
data = df[p1_selected_features].reset_index().melt('Year')
data["Year"] = data["Year"].apply(lambda x: str(x))
p1_chart = alt.Chart(data).mark_line().encode(
    alt.X("Year"),# axis=alt.Axis(domain=False, format='%Y', tickSize=0)),
    # x='Year',
    y='value',
    color='variable'
).properties(width=600, height=250)
st.altair_chart(p1_chart)

############## PLOT 3 #######################
# print(df)

st.markdown("###### We closely observe the distribution of each feature value in all the songs popular songs each year")

def get_modified_df (df_unagg, feat):
    # print(df_unagg)
    
    years = range(2010, 2020)
    datas = []
    for year in years:
        col = df_unagg[df_unagg["Year"]==year]
        # data.append(col.tolist())
        datas.append(col[feat])
    
    df_concat = pd.concat(datas, axis=1)
    df_concat.columns=years
    # print(df_concat)
    return df_concat

allcols= [st.columns(2), st.columns(2), st.columns(2)]

for i in range(len(p1_selected_features)):
    p3_selected_feature = p1_selected_features[i] 
    p3_violin_df = get_modified_df(df_unagg, p3_selected_feature)
    # print(p3_violin_df)
    # print(i, i//2, i%2)
    with allcols[i//2][i%2]:
    # p3_violin_df["color"] = "green"
        fig = px.violin(
                p3_violin_df,orientation='h', color_discrete_sequence=["green"],  labels={'variable':'Year', 'value':p3_selected_feature}
            ).update_traces(
                side="positive", width=5, meanline_visible=True, hoveron= "kde", hoverinfo='x'
            ).update_layout(
                hovermode="closest"
            )
        fig.update_layout(width=400)

        st.plotly_chart(fig,height=20)


