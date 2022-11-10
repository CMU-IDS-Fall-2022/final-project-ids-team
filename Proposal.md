# Final Project Proposal

**GitHub Repo URL**: https://github.com/CMU-IDS-Fall-2022/final-project-ids-team

## Song Popularity Analysis

**Team** 
* Vrinda Jindal
* Liyan Chang
* Haoyu Qi
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


**Sketches and Data Analysis**

***Data Processing***

*Spotify Top 50 songs from 2010-2019 - by year*

General statics:
    
![2-overview](./images/eda-2/overview.png)

* Do you have to do substantial data cleanup? 
    - In this curated dataset, there are no missing values. Hence, not much data cleanup was required. Also, upon loading the dataset, all numerical values were detected as such. The maximum and minimum values of all the features appeared to lie within a reasonable range (no outliers). The first column (index) was dropped. 

    The distribution of number of songs across years is not uniform. To enable uniformity, we will select the top k songs by "pop", i.e. popularity. k here being the least number of songs in any year, which is 2018.

    ![year](./images/eda-2/year.png)


* What quantities do you plan to derive from your data? 
    - This dataset examines the most popular songs. In this case, the popularity column is less important, as we are more interested in the actual characteristics of these features. In particular, the musical features returned by the Spotify API are the quantities we plan to focus on. Some features show high correlation, for example Energy(nrgy) and Loudness(dB).

    ![corr](./images/eda-2/pearsons_2.png)

* How will data processing be implemented?  
    - We will aggregate the data by the year, and take average of musical features to make yearwise plots. Other filtering operations can be conducted by simple pandas changes.

***System Design***

- Why are these songs popular?  
  
For this problem, we decide to use the heat map showing the correlation matrix between each numerical variables and the popularity index(given from the dataset). The color of the map shows the magnitude of the correlation coefficient between the variables. We will provide the users the choices of the features they want to explore. The sketch for this question is shown as below.

 <div align=center><img width="200" height="250" src="https://github.com/CMU-IDS-Fall-2022/final-project-ids-team/blob/main/images/sketch1.jpeg"/></div>
 
 - How can we see the change of the trend?  
 
 For this problem, we provide users checkboxes to select features they are interested in, for example, energy, genre and so on. We then show them the change of the features they select accoring to the change of time. And they can also choose another feature as a key for different groups, for instance, users can choose genre as a group key and choose energy as the feature they want to explore, and we'll show them the change of the energy of popular country music, R&B music, hip-hop music and so on.  
 ![trend](./images/trend.jpg)
 
 - Recommendation

For recommendation, we allow users two kinds of input, either directly the name of song or enter each feature they want. We will use Spotify API or recommendation algorithm to give them top 10 similar songs and a report of the average feature values across different years. A sketch is given below.

 <div align=center><img width="800" height="600" src="https://github.com/CMU-IDS-Fall-2022/final-project-ids-team/blob/main/images/IDSSketch.png"/></div>
 
 
