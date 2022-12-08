# Final Project Report

**Project URL**: TODO
**Video URL**: TODO

Short (~250 words) abstract of the concrete data science problem and how the solutions addresses the problem.

## Introduction

## Related Work
Spotify is without a doubt one of the dominant music streaming platforms over the last few years with millions of users. With the increasing interest to Spotify, there more attempts to visualize the Spotify data. Most of the projects focus on exploring the user’s listening preferences and patterns by visualizing the user’s personal streaming history. In view of the popularity of Spotify data, many application programming interface and packages have been researched to better access the data and visualize the data.


​	As the goal of our project are provide insight of the music preferences and popularity patterns for both music producers and music lovers, we need two main techniques: pattern visualization and recommendation based on edge map.

​	Rshiny app [1] provides users a platform to help them self-explore their listening patterns and music personality based on Spotify and R. As accessing the users’ data without the consent of users and platforms is dangerous and may contain moral hazard, we borrow the idea from Rshiny app to visualize the pattern of top popular music. The author provides a sentiment analysis for the songs. The sentiments contain various attributes of music: ‘danceability’, ‘energy’, ‘loudness’, ‘speechness’, ‘liveness’, and ‘tempo’. A ridgeline chart[2] is used in the sentiment analysis. Ridgeline plots are very helpful when we want to visualize the distribution of categorical variable over time and space. It allows a number of data segments to be plotted on the same horizontal scale with the presentation with slight overlap. Ridgeline plot is ideal to visualize the pattern in the data as it works well to show the direct distribution patterns when there is a clear pattern in the results and it would get messy when there does not exist clear pattern and the groups tend to overlap each other too much [3]. Besides, it is also crucial to present collective sentiment to juedge the music personality. Inspired by the personality analysis [4]. The author from [1] choose two featrues he is interested in and draw a scatter plot based on the two features to get some insight into the music personalities. The example he provided is speechiness vs danceability. A high score of speechiness implies that the song is more wordy such as rap music or spoken word music with minimal instruments. Danceability describes how suitable a track for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength and overall regularity [5]. A scatter plot is useful to observe and visaully discover the correlational relationship between the variables. The visualized relationship could be linear or non-linear, strong or weak, positive or negative [6].  

​	Algorithmic recommendations is now taking center stage in the music discovery landscape.Spotify itself employs several independent ML models and algorithms to generate item representations and user representations to build machine learning models for recommender systems. The representative of track is made up of two components: content-based filtering which evaluates the track by exploring the features of itself; colaborative filtering which takes advantage of user generated assets to build the connection between the track and other tracks on the platform. The original content-based filtering algorithm analyzed the artist-sourced metadata, the high-evel sonic characteristics of the track extracted from the raw audio signs, and semantic information from music-related text content with the utilization of Natural Language Processing modesl [7]. Collaborative filtering takes advantage of the so-called similarity score between the songs and users. There are mainly two ways to compute the similarity score. One is based on a massive user-item interaction matrix covering all users and tacks on the platform, which could be very expensive and time-consuming to mantain. And the other one is more efficient, which is based on a track's organizational similarity such as the two songs are put on the same playlist. As both user profiles and tack profiles are now accesible, Spotify use a recommender system with the reward system to select and generate the recommended playlist for the users. 

​	Explorify [8] is introduced as a visualization tool to achieve the functsions of both exploring the uses' own music tastes by allowing the users to engage with their data. Explorify is user friendly as it assume that the audience do not have specific genre knowledge, audio features and it does not require the users to have expert knowledge in interpreting complex virtualizations. The centerpiece of Explorify is the artist-genre network. Through presenting this network, the authors wish to show the connection between the genre and artists. The authors choose to use an edge map to visualize the artist-genre network. A force-directed layout is employed to guarantee the interactivity and clarity of the nodes in the virtualization. Color of a node is closely related with the polar coordinates in the edgemap. Edge connects two nodes and the relationship represented by the edges is commutative. The lable of the artist is hovered at the top of the node and it can be hidden in the generated virtualization. Edgemap which visually presenting a network of connecting entities builds a node-link model. It is intuitive, flexible, fast and insightful by allowing users to gain deeper knowledge, undersgtand the context and finding something they are interested in by diving into the map.   

​	Refering to the similarity score, the similarity metrics can be divided into two groups: similarity based metrocs and distance based metrics. The first category determine the most similar objects with the highest values. The commonly used metrics are Pearsin's correlation coefficient which is a measure related to the strength and direction of a linear relationship; Spearman's correlation which uses the rank of each value; Kendall's Tau which is quite similar to Spearman's correlation; Cosine similarity calculates the consine of the angle between two vectors; while Jaccard similaroty compares two binary vectors. On the other hand, the distance based methods choose the most similar objects by prioritizing objects with lowest values. The most common method is using Euclidean distance which is also called straight-line distance between two vectors. The other one is Manhattan distance which is also know as 'cityblock'.
## Methods

## Results

## Discussion

## Future Work

## Reference
[1] Barlas, A. (2021, November 29). Combining Spotify and R - an interactive Rshiny app + spotify dashboard tutorial. Medium. Retrieved December 6, 2022, from https://towardsdatascience.com/combining-spotify-and-r-an-interactive-rshiny-app-spotify-dashboard-tutorial-af48104cb6e9 


[2] Holtz, Y. (n.d.). Ridgeline Chart. the R Graph Gallery. Retrieved December 6, 2022, from https://r-graph-gallery.com/ridgeline-plot.html 

[3] Healy, Y. H. and C. (n.d.). Ridgeline plot. Ridgeline plot – from Data to Viz. Retrieved December 6, 2022, from https://www.data-to-viz.com/graph/ridgeline.html 

[4] Pham, J. (2021, October 4). Spotify personal data analysis. Medium. Retrieved December 6, 2022, from https://medium.com/@joypham7/spotify-personal-data-analysis-858c8fbe6983 

[5] Patients choose music with high energy, danceability, and lyrics in ... (n.d.). Retrieved December 6, 2022, from https://journals.sagepub.com/doi/10.1177/0305735620907155 

[6] Scatter plot. Corporate Finance Institute. (2022, November 5). Retrieved December 6, 2022, from https://corporatefinanceinstitute.com/resources/data-science/scatter-plot/ 

[7] How Spotify's algorithm works? A Complete Guide to spotify recommendation system [2022]: Music tomorrow blog. How Spotify's Algorithm Works? A Complete Guide to Spotify Recommendation System [2022] | Music Tomorrow Blog. (n.d.). Retrieved December 6, 2022, from https://www.music-tomorrow.com/blog/how-spotify-recommendation-system-works-a-complete-guide-2022#:~:text=%22We%20can%20understand%20songs%20to,recommend%20song%20Z%20to%20them. 

[8] Ivanova, I., &amp; Engstad, J. (n.d.). Explorify: A Personalized Interactive Visualization Tool for Spotify Listening History. CPSC 547: Information visualization, Sep 2021. Retrieved December 6, 2022, from https://www.cs.ubc.ca/~tmm/courses/547-21/ 
