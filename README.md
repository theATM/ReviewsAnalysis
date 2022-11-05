# ReviewsAnalysis
**Analysis of Online Reviews of Parking Mobile apps using NLP and Technology Acceptance Models (TAM)**

This is the code repository for the project created for course Natural Language Processing and Text Mining in the Autumn of 2022.

Project consist of four jupyter notebooks designed to do the 8 tasks defined in the assigment requirements

For task 1 to 4 please run scrapper.ipynb.
For task 5 run topic.ipynb.
For task 6 run training.ipynb.
For tasks 7 and 8 run TAM.ipynb.

Additionally, to the notebooks there are .py files which contain necessary functions and classes, but are not ment to be executed on its own.

## Assigment requirements:
In this project, the students will collect Thousands of online reviews from Apple and Google Play stores from
across Europe or at least Nordic area, to understand how users react to emergency apps that run in the Nordic
region – 112 Suomi, and Emergency SOS, EmergencyPlus. Feel free to add or amend if not enough reviews
were collected. This project will provide insight into user behavior, sentiment toward emergency apps and
highlight the most important topics regarding users' requests, demands and preferences in terms of emergency
solutions or technology features.
1. Write a script to download data for the two apps and save them in CSV files separately. Data collection
involves getting user IDs, reviews, reviews’ ratings, reviews’ dates, and version history of the apps
from Google play and Apple store. Additionally, you can collect other information if you wish.
2. Ensure that all reviews are translated into English, clean the data, and process it. Concatenate the data
from both stores but keep the two apps' data separate in two data-frames for further analysis. At the end
you would have separate datasets, one for each App.
The following tasks are to be performed for each app separately, except for 6, 7, 8, and 12 which are common to
all:
3. Perform the sentiment analysis of the reviews and try to classify each review as either positive (1),
negative (-1), or neutral (0). You can use sentiment Vader (https://github.com/cjhutto/vaderSentiment)
and use the compound results to make the classification by specifying thresholds. Add the sentiment
results to a distinct column in your datasets (data-frames).
   - positive sentiment: compound score >= 0.05
   - neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
   - negative sentiment: compound score <= -0.05
4. Consider making two plots, one for ratings and another for sentiments over time. Use the date
about new versions and new releases. Scatter these dates across each plot so you can observe
the effect of the new version on the sentiment or rating.
5. We want to find the most discussed topics from users, and for that, perform LDA topic modeling and try
to generate 10 topics.
6. Train a machine learning model (random forest or another one) with positive and negative sentiment
reviews. Try to use different n-gram representations such as n-gram (2,3) or (3,4). Then perform feature
selection to identify the most important words or n-gram elements that impacted the classification for
positive and negative classes. Try to specify the class for each word or element you retrieve.
7. The next task is about the use of technology acceptance models (TAM) to assess how people respond to
technology adoption decisions. For instance, we try to measure the level of satisfaction, perceived ease
of use, perceived usefulness, and attitudes toward the technology
   - 7.1. Try to learn more about TAM from this review paper [1]. We are interested in understanding how the
   indicators: perceived ease of use, perceived usefulness, satisfaction, attitude, and behavioral
   intentions change over time. You can check this paper [2] as well for more information about some of
   the TAM indicators.
   - 7.2. Generate keyword lists for each indicator based on your understanding of the topic. For instance: some
   keywords for satisfaction are {Satisfied, fulfill, gratify, meet, beneficial, content, happy, appeasement , etc.}.
   - 7.3. To augment the list of keywords, write a script that finds synonyms, hypernyms, and hyponyms for each
   word, by using WordNet database. Review the words manually and remove those which are not relevant. 
   - 7.4 Perform necessary data processing for the list of keywords and reviews, for instance, Part of Speech
   tagging and lemmatization. Then classify each review and its data (rating, sentiment, and date) to a
   particular TAM indicator based on the common words. In the end, it is expected to have 5 data-frames,
   each one refers to data related to one TAM indicator. 
   - 7.5 Repeat task 4 for each indicator. 
   - 7.6 Calculate the Pearson correlation with a its associated p-value between different indicators and
   determine which are most strongly correlated. Highlight the correlations you find. Provide table to
   summarize your work. 
   - 7.7 If the rating is provided, compute the correlation between the sentiment and rating. Repeat this process
   when you separate between positive and negative sentiment.
8. Identify relevant literature on parking behavior, TAMs, and other associated topics to support and discuss
   what you have found in previous sections.

<sub>
[1]: Koul, S., Eydgahi, A., 2017. A systematic review of technology adoption frameworks and their applications. Journal of technology management&
innovation 12, 106–113.

[2]: Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS quarterly, 319-340.


[3]: Yoon, H. Y. (2016). User acceptance of mobile library applications in academic libraries: an application of the technology acceptance model. The Journal
of Academic Librarianship, 42(6), 687-693.
</sub>