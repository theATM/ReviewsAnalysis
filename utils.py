
import re
import os
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize.casual import TweetTokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer

sentiment_dict = \
{
    "Positive" : 1,
    "Negative" : 0,
    "Neutral"  : -1, #merge neutral to negative
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



def count_data_stat(data):
    positive, negative = 0,0
    for sent in data.sentiment:
        if sent == 0:
            negative +=1
        elif sent == 1:
            positive +=1
    print("Positive :", positive)
    print("Negative :", negative)

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

