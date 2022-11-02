# Final Project Proposal

**GitHub Repo URL**: https://github.com/CMU-IDS-Fall-2022/final-project-ids-team

## Song Popularity Analysis

**Team** 
* Vrinda Jindal
* Liyan Chang
* Haoqu Qi
* Tanvi Karandikar
* Vincie Ju

**Problem Description**

Music is a form of cultural expression. Popular music can been seen as a reflection of an era's cultural identity. Through this project, using data science tools we aim to do a deep dive analysis of popular music across years, answering questions like what makes songs popular and exploring how popular music has changed over the years. We believe such an analysis will not only be interesting from a cultural standpoint but will also be insightful for song creators - helping producers explore on what makes a song popular. We also propose to create an interactive component that recommends music to people based on their preferences by leveraging the power of data and patterns.


**Questions and Solutions**
- Why are these songs popular?
To solve this problem, we decide to explore the features. We will provide the functions to enable the dashboard users to choose the features they are most interested and draw a correlation map of the features and the popularity score. Through viewing the correlation map, we will be able to tell which features contribute to the popularity score. Moreover combined with the distribution of the features, we will be able to tell the propertie of the popular songs.

- How are popular songs change over time?
To help both music producers and listeners to sense the change of the trend, we will provide an analysis of changes of features of popular songs over time. Users can select features they are interested in and we'll visualize the trending genre, danceability and so on and try to offer them some fancy insights.

- Recommendation
To help the music producer get inspiration and music lovers to find more songs of their tastes, we will provide a recommendation system which can take two kinds of input, for producer and lover, respectively. The user can either choose the range of features they want, such as year, danceability, etc, or input several favorite songs. These features will eventually be feed into a recommendation system based on matrix factorization or simply Spotify API to retrieve the top similar songs. A final report will be given based on all the similar songs.  

**Data Sources**
- [Spotify - All Time Top 2000s Mega Dataset](https://www.kaggle.com/datasets/iamsumat/spotify-top-2000s-mega-dataset)
- [Spotify Top 50 songs from 2010-2019 - by year](https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year)
- [Spotify API](https://developer.spotify.com/documentation/web-api/)
- [Spotify Million Playlist Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)