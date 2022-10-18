from app_store_scraper import AppStore
from google_play_scraper import app
from google_play_scraper import Sort, reviews_all

import pandas as pd
import numpy as np
import time  # I shall import time this instance!


def google_scrapp(app_id, language, country, amount):
    google_reviews = reviews_all(
        str(app_id),
        sleep_milliseconds=10,  # defaults to 0
        lang=str(language),  # defaults to 'en'
        country=str(country),  # defaults to 'us'
        sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    )
    google_dataframe = pd.DataFrame(np.array(google_reviews), columns=['review'])
    google_dataframe = google_dataframe.join(pd.DataFrame(google_dataframe.pop('review').tolist()))
    google_dataframe.drop(['userImage', 'repliedAt', 'replyContent'], axis=1, inplace=True)


    return google_dataframe


def apple_scrapp(app_name, app_id, country, how_many):
    appStore_reviews = AppStore(country=str(country), app_name=str(app_name), app_id=str(app_id))
    appStore_reviews.review(how_many=how_many)
    appStore_dataframe = pd.DataFrame(np.array(appStore_reviews.reviews), columns=['review'])
    appStore_dataframe = appStore_dataframe.join(pd.DataFrame(appStore_dataframe.pop('review').tolist()))
    appStore_dataframe.drop(['isEdited', 'userName'], axis=1, inplace=True)
    appStore_dataframe = appStore_dataframe.rename(columns={'review': 'content'})
    return appStore_dataframe


class GoogleTranslator:
    def __init__(self):
        from deep_translator import GoogleTranslator
        self.translator = GoogleTranslator()

    def translate(self, data):
        data['content'] = self.__remove_quotas(data).apply(
            lambda x: self.translator.translate(x, source='auto', target_lang="en"))
        return data

    @staticmethod
    def __remove_quotas(data):
        import re
        return data['content'].apply( lambda x:  re.sub('"','',str(x)) )





