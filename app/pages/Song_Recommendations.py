import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import plotly.express as px
import igraph as ig
import plotly.graph_objects as go
from streamlit_searchbox import st_searchbox

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


# st.title("Let's analyze some heat songs.")

# @st.cache  # add caching so we load the data only once
@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv('data/Spotify-2000.csv')
    # df.fillna(0)
    return df

# @st.cache
@st.cache(allow_output_mutation=True)
def get_slice_data(df, genre):
    if genre != 'others':
        labels = df['Top Genre']==genre
        return labels
    
    labels = ~df['Top Genre'].isin(['album rock', 'adult standards', 'dutch pop', 'alternative rock',
       'dance pop'])
    return labels

# st.write("Please select your interested genre and observe the trend of some features from 60s to the recent.")

df = load_data()


# with st.sidebar:
#     # st.header('Spotify Music Analysis')

# # cols=st.columns(2)

# # with cols[0]:
#     selections = np.array(['album rock', 'adult standards', 'dutch pop', 'alternative rock',
#        'dance pop', 'others'])
#     genre=st.selectbox('Top Genre',selections)
# # with cols[1]:
#     selections = np.array(['Danceability', 'Loudness (dB)',
#        'Liveness', 'Valence', 'Length (Duration)', 'Acousticness',
#        'Speechiness', 'Popularity'])
#     feature = st.selectbox('Feature', selections)

# df_genre = df[get_slice_data(df, genre)]
# d60s = df_genre[(df_genre['Year']>=1959) & (df_genre['Year']<1969)][feature].reset_index(drop=True)
# d70s = df_genre[(df_genre['Year']>=1969) & (df_genre['Year']<1979)][feature].reset_index(drop=True)
# d80s = df_genre[(df_genre['Year']>=1979) & (df_genre['Year']<1989)][feature].reset_index(drop=True)
# d90s = df_genre[(df_genre['Year']>=1989) & (df_genre['Year']<1999)][feature].reset_index(drop=True)
# d00s = df_genre[(df_genre['Year']>=1999) & (df_genre['Year']<2009)][feature].reset_index(drop=True)
# d10s = df_genre[(df_genre['Year']>=2009) & (df_genre['Year']<2019)][feature].reset_index(drop=True)

# colnames = ['60s', '70s', '80s', '90s', '00s', '10s']
# df_concat = pd.concat([d60s, d70s, d80s, d90s, d00s, d10s], axis=1)
# df_concat.columns=colnames

# st.plotly_chart(
#     px.violin(
#         df_concat,orientation='h',labels={'variable':genre, 'value':feature}
#     ).update_traces(
#         side="positive", width=5, meanline_visible=True, hoveron= "kde", hoverinfo='x'
#     ).update_layout(
#         hovermode="closest"
#     )
# )

st.write("Please search your favorite song, and we can make recommendation for you.")
titles = df['Title'].to_list()
# print(titles[0])
def search_wikipedia(searchterm):
    searchterm = searchterm.strip().lower()
    return [track for track in titles if searchterm in track.lower()] if searchterm else []


# pass search function to searchbox
selected_value = st_searchbox(
    search_wikipedia,
    key="wiki_searchbox",
)

if selected_value:
    # selected_value = 'Sunrise'
    # print(df['Title'==selected_value]['Top Genre'])
    if df[df['Title']==selected_value]['Top Genre'].to_list()[0] in ['album rock', 'adult standards', 'dutch pop', 'alternative rock', 'dance pop']:
        genre_edge = df[df['Title']==selected_value]['Top Genre'].to_list()[0]
    else:
        genre_edge = 'others'
    # st.markdown("You've selected: %s" % selected_value)

    st.write("The song you are inspecting is", selected_value, 'and its genre falls in', genre_edge)
    selections = np.array(['Danceability', 'Loudness (dB)',
        'Liveness', 'Valence', 'Length (Duration)', 'Acousticness',
        'Speechiness', 'Popularity'])
    feature = st.selectbox('Choose a feature we can recommend based on.', selections)

    # Edgemap Plot

    def map_function(x): # Return Years
        if df['Year'].min()<= x <1969        : return '60s'
        elif 1969<=x<1979      : return '70s'
        elif 1979<= x <1989   : return '80s'
        elif 1989<= x <1999  : return '90s'
        elif 1999<=x < 2009  : return '00s'
        elif 2009<=x<=2019    :return  '10s'

    def get_top5_idx(A): # return top similar tracks
        top5_idx = []
        for row in A:
            sort = sorted(row, reverse=True)
            top5_idx.append(np.where((row <= sort[1]) & (row >=sort[min(5, np.count_nonzero(sort)-1)])))
        return top5_idx

    def convert(a): # Return adjacency list and weight/year list
        adjList = []
        weightList = []
        eralist = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                    if a[i][j] != 0. and i < j:
                        adjList.append((i, j))
                        weightList.append(a[i][j]**2)
                        idx = np.random.choice([i,j])
                        eralist.append(df_genre['Era'].to_list()[idx])
        return adjList, weightList, eralist

    # print(genre_edge)
    df_genre = df[get_slice_data(df, genre_edge)].copy()
    df_genre['Era']=df_genre['Year'].apply(map_function)
    # df_genre = df[df['Top Genre'] == genre]
    diff = np.abs(df_genre[feature].values - df_genre[feature].values[:,None])
    diff_norm = 1-((diff-diff.min())/(diff.max()-diff.min()))
    diff_norm[diff_norm<0.97] = 0
    np.fill_diagonal(diff_norm, 0)
    idx = np.nonzero(diff_norm)
    diff_norm[idx] = (diff_norm[idx]-np.min(diff_norm[idx]))/(np.max(diff_norm[idx])-np.min(diff_norm[idx]))
    np.fill_diagonal(diff_norm, 0)

    AdjList, WeightList, Eralist = convert(diff_norm)
    g = ig.Graph(len(diff_norm), AdjList)
    g.vs["name"] = list(df_genre['Title'])
    g.vs['Era'] = list(df_genre['Era'])
    N=len(diff_norm)
    E=[e.tuple for e in g.es]# list of edges
    layt=g.layout() #kamada-kawai layout

    Xn=[layt[k][0] for k in range(N)]
    Yn=[layt[k][1] for k in range(N)]

    # Edge trace
    trace1 =  [dict(type='scatter',
                x=[layt[e[0]][0], layt[e[1]][0], None],
                y=[layt[e[0]][1], layt[e[1]][1], None],
                mode='lines',
                opacity=w,
                showlegend=False,
                legendgroup = era,
                line=dict(width=1, color='rgb(150,150,150)')) for e, w, era in zip(E, WeightList, Eralist)]
            
    axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
            )

    # width=800
    height=600
    layout=go.Layout(
        font= dict(size=12),
        autosize=False,
        # width=width,
        height=height,
        xaxis=go.layout.XAxis(axis),
        yaxis=go.layout.YAxis(axis),
        # margin=go.layout.Margin(
        #     l=20,
        #     r=20,
        #     b=45,
        #     t=50,
        # ),
        hovermode='closest'
        )

    fig=go.Figure(data=trace1, layout=layout)

    col_list = {'60s': '#11150d',
                '70s': '#314026',
                '80s': '#314026',
                '90s': '#739559',
                '00s': '#94bf73',
                '10s': '#b5ea8c'}

    for i, p in enumerate(['60s','70s','80s','90s','00s','10s']):
        idx = np.where(np.array(df_genre['Era'].to_list()) == p)[0]
        top5_idx = get_top5_idx(diff_norm[idx])
        top5_track = [np.array(df_genre['Title'].to_list())[i] for i in top5_idx]
        hovertext = ['<b>Song Track: </b>'+str(x)+'<br><b>Top Similar Tracks: </b><br>'+'<br>'.join(y) for x,y in zip(np.array(df_genre['Title'].to_list())[idx], top5_track)]
        fig.add_trace(go.Scatter(
            x=np.array(Xn)[idx],
            y=np.array(Yn)[idx],
            mode='markers',
            name=p,
            legendgroup=p,
            marker=dict(symbol='circle-dot',
                        size=10,
                        color = col_list[p]
                        ),
            text=hovertext,
            hoverinfo='text'
        ))

    select_idx = np.where(np.array(df_genre['Title'].to_list()) == selected_value)[0]
    # print(select_idx, np.array(Xn)[select_idx], np.array(Yn)[select_idx])
    fig.add_annotation(
        x=np.array(Xn)[select_idx][0],
        y=np.array(Yn)[select_idx][0],
        showarrow=False,
        xshift=10,
        text="<b>"+selected_value+"</b>")
    fig.update_layout(legend_title_text='Year')

    st.plotly_chart(fig, use_container_width=True)


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
