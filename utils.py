
import re
import os
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize.casual import TweetTokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer

labels_dict = \
{
    "Positive" : 1,
    "Negative" : 0,
    "Neutral"  : -1, #swap neutral to negative
}

sentiment_dict = \
{
    "Positive": 1,
    "Neutral": 0,
    "Negative": -1,
}

souce_type_dict = \
{
    "Suomi112_google" : 0,
    "Suomi112_apple" : 1,
    "SosLive_google" : 2,
    "SosLive_apple" : 3,
}

class Processor:
    def __init__(self):
        self.tokenizer = TweetTokenizer()
        self.stemmer = SnowballStemmer(language='english')
        self.lemanizer = WordNetLemmatizer()

    @staticmethod
    def ini_dowload():
        # dowload all the nessesary files to do the preprocesing (like the dictionary of the stopwords
        nltk.data.path.append('data' + os.sep + "lib" + os.sep + 'stopwords')
        nltk.download("stopwords", download_dir="data" + os.sep + "lib" + os.sep + "stopwords")
        nltk.data.path.append('data' + os.sep + "lib" + os.sep + 'wordnet')
        nltk.download('wordnet', download_dir="data" + os.sep + "lib" + os.sep + "wordnet")
        nltk.data.path.append('data' + os.sep + "lib" + os.sep + 'omw')
        nltk.download("omw-1.4", download_dir="data" + os.sep + "lib" + os.sep + "omw")

    @staticmethod
    def preprocess(text: str): # First setep
        # Used to get rid of the unnesesary characters and to stringify the emogis
        text = text.lower()
        text = emoji.demojize(text)
        text = re.sub('[\',:;.!?_\-()=+|{}\[\]<>#\\\/\"\n\r~`]',' ',text)
        text = re.sub('[$%&@0-9]', '', text)
        return text

    def tokenize(self, text: str): # Second setep
        return self.tokenizer.tokenize(text)

    @staticmethod
    def remove_stopwords(tokens,remove_len=3): # Third setep
        return [word for word in tokens if word not in stopwords.words("english") and len(word) > remove_len]

    def process_tokens(self, tokens): # Fourth setep
        new_tokens = []
        for token in tokens:
            if token not in stopwords.words("english"):
                new_tokens.append(self.stemmer.stem(self.lemanizer.lemmatize(token, pos='v')))
        return new_tokens

    def detokenize(self,tokens): # Only use if nesesary
        return ' '.join(tokens)

    def not_no(self,tokens):
        return [token if token!= "no" else "negation" for token in tokens]



def count_data_stat(data,use_labels=True):
    positive, negative, neutral = 0,0,0
    positive_label = labels_dict["Positive"] if use_labels else sentiment_dict["Positive"]
    neutral_labels = labels_dict["Neutral"] if use_labels else sentiment_dict["Neutral"]
    negative_labels = labels_dict["Negative"] if use_labels else sentiment_dict["Negative"]
    for sent in data.sentiment:
        if sent == negative_labels:
            negative +=1
        elif sent == positive_label:
            positive +=1
        elif sent == neutral_labels:
            neutral +=1
    print("Positive :", positive)
    print("Negative :", negative)
    if neutral > 0 :
        print("Neutral :", neutral)

    d1g, d1a, d2g, d2a = 0,0,0,0
    for type in data.type:
        if type == 0:
            d1g +=1
        elif type == 1:
            d1a +=1
        elif type == 2:
            d2g +=1
        elif type == 3:
            d2a +=1
    print("Suomi112 google :", d1g)
    print("Suomi112 apple :", d1a)
    print("SosLive google :", d2g)
    print("SosLive apple :", d2a)

