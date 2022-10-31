import pandas as pd
import numpy as np


def date_conversion(dataframe):
    dataframe['at'] = pd.to_datetime(dataframe['at']).dt.floor('D')


def rating_graph(dataframe):
    date_conversion(dataframe)
    new_frame = dataframe.groupby(dataframe['reviewCreatedVersion']).agg({'score': np.mean, 'at': np.min})
    new_frame.plot(x='at', y='score', kind='bar', xlabel='Version release', ylabel='Version Average Rating', title='Relationship between Average Rating and App Versions')


def sentiment_graph(dataframe):
    date_conversion(dataframe)
    new_frame = dataframe.groupby(dataframe['reviewCreatedVersion']).agg({'sentiment': np.mean, 'at': np.min})
    new_frame.plot(x='at', y='sentiment', kind='bar', xlabel='Version release', ylabel='Version Average Sentiment', title='Relationship between Average Sentiment and App Versions')


def sentiment_rating_graph(dataframe):
    dataframe.groupby(dataframe['score'])['sentiment'].mean().plot(
        kind='bar', rot=0, xlabel='Score', ylabel='Sentiment', title='Relationship between Rating and Sentiment')
