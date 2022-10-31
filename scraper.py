from app_store_scraper import AppStore
from google_play_scraper import Sort, reviews_all
import pandas as pd
import numpy as np


def google_scraper(app_id, language, country):
    google_reviews = reviews_all(
        str(app_id),
        sleep_milliseconds=100,  # defaults to 0
        lang=str(language),  # defaults to 'en'
        country=str(country),  # defaults to 'us'
        sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    )
    google_dataframe = pd.DataFrame(np.array(google_reviews), columns=['review'])
    google_dataframe = google_dataframe.join(pd.DataFrame(google_dataframe.pop('review').tolist()))
    google_dataframe.drop(['userImage', 'repliedAt', 'replyContent', 'reviewId', 'thumbsUpCount'], axis=1, inplace=True)

    return google_dataframe


def apple_scraper(app_name, app_id, country, how_many):
    appstore_reviews = AppStore(country=str(country), app_name=str(app_name), app_id=str(app_id))
    appstore_reviews.review(how_many=how_many)
    appstore_dataframe = pd.DataFrame(np.array(appstore_reviews.reviews), columns=['review'])
    appstore_dataframe = appstore_dataframe.join(pd.DataFrame(appstore_dataframe.pop('review').tolist()))
    appstore_dataframe.drop(['isEdited', 'title'], axis=1, inplace=True)
    appstore_dataframe = appstore_dataframe.rename(columns={'review': 'content', 'rating': 'score', 'date': 'at'})
    return appstore_dataframe


