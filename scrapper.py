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
    appStore_dataframe = appStore_dataframe.join(pd.DataFrame(appStore_dataframe.pop('review').tolist()))
    appStore_dataframe.drop(['isEdited', 'userName'], axis=1, inplace=True)
    appStore_dataframe = appStore_dataframe.rename(columns={'review': 'content'})
    return appStore_dataframe


class Translator:
    def __init__(self,model_type='opus-mt',arg_device='cuda',cache_folder="cache/transformers"):
        from easynmt import EasyNMT
        import os
        from torch import cuda, device
        if arg_device == 'cuda':
            cuda.empty_cache()
        self.device = device(arg_device)  # change to cpu if you do not have a gpu else cuda
        self.model_fi = EasyNMT('opus-mt', cache_folder=cache_folder, device=self.device)
        #self.model_sw = EasyNMT('mbart50_m2en', cache_folder=cache_folder, device=self.device)

    def translate_fi(self,scrapped_data):
        scrapped_data['translatedContent'] = scrapped_data['content'].apply(lambda x: self.model_fi.translate(x, target_lang="en", source_lang="fi", max_length=512))
        return scrapped_data

    def deactivate(self):
        from torch.cuda import empty_cache
        if self.device == 'cuda':
            empty_cache()
        del self.model_fi
        del self.model_sw


class GoogleTranslator:
    def __init__(self):
        from deep_translator import GoogleTranslator
        self.translator = GoogleTranslator()

    def translate(self, scrapped_data):
        scrapped_data['translatedContent'] = scrapped_data['content'].apply(
            lambda x: self.translator.translate(x, source='auto', target_lang="en"))
        return scrapped_data




