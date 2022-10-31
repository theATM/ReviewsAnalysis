from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def compound_score(dataframe):
    analyzer = SentimentIntensityAnalyzer()
    dataframe['content'] = dataframe['content'].fillna('')  # To avoid errors when iterating
    dataframe["sentiment"] = ""

    for index, row in dataframe.iterrows():
        compound_result = analyzer.polarity_scores(row['content'])['compound']

        if compound_result >= 0.05:
            dataframe.at[index, 'sentiment'] = 1
        elif -0.05 < compound_result < 0.05:
            dataframe.at[index, 'sentiment'] = 0
        else:
            dataframe.at[index, 'sentiment'] = -1

