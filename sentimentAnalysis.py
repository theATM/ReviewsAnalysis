import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def compound_score(dataframe):
    analyzer = SentimentIntensityAnalyzer()
    dataframe['content'] = dataframe['content'].fillna('')  # To avoid errors when iterating
    dataframe["sentiment"] = ""

    for index, row in dataframe.iterrows():
        compoundresult = analyzer.polarity_scores(row['content'])['compound']

        if compoundresult >= 0.05 :
            dataframe.at[index, 'sentiment'] = "Positive"
        elif -0.05 < compoundresult < 0.05:
            dataframe.at[index, 'sentiment'] = "Neutral"
        else:
            dataframe.at[index, 'sentiment'] = "Negative"

    print("End of analysis")
