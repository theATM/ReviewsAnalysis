
import re
import os
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize.casual import TweetTokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer

class Processor:
    def __init__(self):
        self.tokenizer = TweetTokenizer()
        self.stemmer = SnowballStemmer(language='english')
        self.lemanizer = WordNetLemmatizer()

    @staticmethod
    def ini_dowload():
        nltk.data.path.append('data' + os.sep + "lib" + os.sep + 'stopwords')
        nltk.download("stopwords", download_dir="data" + os.sep + "lib" + os.sep + "stopwords")
        nltk.data.path.append('data' + os.sep + "lib" + os.sep + 'wordnet')
        nltk.download('wordnet', download_dir="data" + os.sep + "lib" + os.sep + "wordnet")
        nltk.data.path.append('data' + os.sep + "lib" + os.sep + 'omw')
        nltk.download("omw-1.4", download_dir="data" + os.sep + "lib" + os.sep + "omw")

    @staticmethod
    def preprocess(text: str):
        text = text.lower()
        text = emoji.demojize(text)
        text = re.sub('[\',:;.!?_\-()=+|{}\[\]<>#\\\/\"\n\r~`]',' ',text)
        text = re.sub('[$%&@0-9]', '', text)
        return text

    def tokenize(self, text: str):
        return self.tokenizer.tokenize(text)

    @staticmethod
    def remove_stopwords(tokens):
        return [word for word in tokens if word not in stopwords.words("english") and len(word) > 3]

    def process_tokens(self, tokens):
        new_tokens = []
        for token in tokens:
            if token not in stopwords.words("english"):
                new_tokens.append(self.stemmer.stem(self.lemanizer.lemmatize(token, pos='v')))
        return new_tokens


