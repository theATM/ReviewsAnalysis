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


class Translator:
    def __init__(self,model_type='opus-mt',device='cuda',cache_folder="cache/transformers"):
        from easynmt import EasyNMT
        import os
        import torch
        self.device = torch.device(device)  # change to cpu if you do not have a gpu else cuda
        self.model_fi = EasyNMT('opus-mt', cache_folder=cache_folder, device=device)
        #self.model_sw = EasyNMT('mbart50_m2en', cache_folder=cache_folder, device=device)

    def translate(self,scrapped_data):
        scrapped_data['translatedContent'] = scrapped_data['content'].apply(lambda x: self.model_fi.translate(x, target_lang="en", source_lang="fi", max_length=512))
        #scrapped_data['translatedContent'] = scrapped_data['translatedContent'].apply(lambda x: self.model_sw.translate(x, target_lang="en", source_lang="sw", max_length=512))
        return scrapped_data



