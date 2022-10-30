import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from packaging import version
from datetime import datetime
import matplotlib.pyplot as plt


def compound_score(dataframe):
    analyzer = SentimentIntensityAnalyzer()
    dataframe['content'] = dataframe['content'].fillna('')  # To avoid errors when iterating
    dataframe["sentiment"] = ""

    for index, row in dataframe.iterrows():
        compoundresult = analyzer.polarity_scores(row['content'])['compound']

        if compoundresult >= 0.05:
            dataframe.at[index, 'sentiment'] = 1
        elif -0.05 < compoundresult < 0.05:
            dataframe.at[index, 'sentiment'] = 0
        else:
            dataframe.at[index, 'sentiment'] = -1

    print("End of analysis")


def date_conversion(dataframe):
    dataframe['at'] = pd.to_datetime(dataframe['at']).dt.floor('D')


def rating_graph(dataframe):
    date_conversion(dataframe)
    newframe = dataframe.groupby(dataframe['reviewCreatedVersion']).agg({'score': np.mean, 'at': np.min})
    newframe.plot(x='at', y='score', kind='bar', xlabel='Version release', ylabel='Version Average Rating')


def sentiment_graph(dataframe):
    date_conversion(dataframe)
    newframe = dataframe.groupby(dataframe['reviewCreatedVersion']).agg({'sentiment': np.mean, 'at': np.min})
    newframe.plot(x='at', y='sentiment', kind='bar', xlabel='Version release', ylabel='Version Average Sentiment')
