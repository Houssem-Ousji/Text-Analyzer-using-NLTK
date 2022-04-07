from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download("book")
nltk.download('omw-1.4')
class Doc:
    def __init__(self,name,path):
        self.name = name
        self.path = path
    def __read(self):
        return open(self.path,"r").read()
    def word_tokenization(self):
        return word_tokenize(self.__read())
    def line_tokenization(self):
        return sent_tokenize(self.__read())
    def delete_stop_words(self):
        stop_words = set(stopwords.words('english'))
        word_tokens = self.word_tokenization()
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        return filtered_sentence
    def racinisation(self):
        ps = PorterStemmer()
        rac = []
        for word in self.delete_stop_words():
            rac.append(ps.stem(word))
        return rac
    def lemmatisation(self):
        lemmatizer = WordNetLemmatizer()
        lemm = []
        for word in self.delete_stop_words():
            lemm.append(lemmatizer.lemmatize(word))
        return (lemm)
    def labeling(self):
        Etiq = []
        try:
            for i in self.delete_stop_words():
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                Etiq.append(tagged)
        except Exception as e:
            print(str(e))
        return (Etiq)
