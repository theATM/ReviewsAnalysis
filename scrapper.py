from app_store_scraper import AppStore
from google_play_scraper import app
from google_play_scraper import Sort, reviews_all

import pandas as pd
import numpy as np


def google_scrapp(app_id,country):
    google_reviews = reviews_all(
        str(app_id),
        sleep_milliseconds=0,  # defaults to 0
        lang='en',  # defaults to 'en'
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
    return appStore_dataframe



#def data_scrapp():
#    googlePlay_suomi112_reviews = reviews_all(
#        'fi.digia.suomi112',
#        sleep_milliseconds=0,  # defaults to 0
#        lang='en',  # defaults to 'en'
#        country='fi',  # defaults to 'us'
#        sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
#    )
#    googlePlay_suomi112_dataframe = pd.DataFrame(np.array(googlePlay_suomi112_reviews), columns=['review'])
#
#    googlePlay_plus_reviews = reviews_all(
#        'com.threesixtyentertainment.nesn',
#        sleep_milliseconds=0,  # defaults to 0
#        lang='en',  # defaults to 'en'
#        country='fi',  # defaults to 'us'
#        sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
#    )
#
#    appStore_suomi112 = AppStore(country='fi', app_name='112 Suomi', app_id='998281396')
#    appStore_suomi112.review(how_many=100)
#    appStore_suomi112_dataframe = pd.DataFrame(np.array(appStore_suomi112.reviews), columns=['review'])
#
#    appStore_plus = AppStore(country='fi', app_name='Emergency Plus', app_id='691814685')
#    appStore_plus.review(how_many=100)

