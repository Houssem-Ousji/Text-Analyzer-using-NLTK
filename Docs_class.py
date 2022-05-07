import nltk
from math import log
nltk.download("book")
nltk.download('omw-1.4')
class Docs():
    def __init__(self,*doc_list):
        self.doc_list = doc_list
    def doc_hote(self, word):
        res = []
        for doc in self.doc_list:
            if word in doc.racinisation():
                res.append(doc.name)
        return res
    def word_frequency(self, word):
        res = []
        for doc in self.doc_list:
            if doc.name in self.doc_hote(word):
                all_words = []
                for w in doc.racinisation():
                    all_words.append(w.lower())
                all_words = nltk.FreqDist(all_words)
                res.append((word,all_words[word],doc.name))
        return res
    def weight(self, word):
        res = []
        for doc in self.doc_list:
            if doc.name in self.doc_hote(word):
                all_words = []
                for w in doc.racinisation():
                    all_words.append(w.lower())
                all_words = nltk.FreqDist(all_words)
                formule = (1+log(all_words[word]))*log(len(self.doc_list) / len(self.doc_hote(word)))
                res.append((word,formule,doc.name))
        return res
    def tf_idf(self,word):
        texts = []
        for doc in self.doc_list:
            if doc.name in self.doc_hote(word):
                texts.append(doc.racinisation())
        mytexts = nltk.TextCollection(texts)
        tf = []
        for t in texts:
            for doc in self.doc_list:
                if doc.racinisation() == t:
                    tf.append((mytexts.tf(word, t),doc.name))
                    continue
        return tf
    def most_relevant(self, word):
        tf_idf = self.tf_idf(word)
        max = tf_idf[0][0]
        doc = tf_idf[0][1]
        for i in range(1,len(tf_idf)):
            if tf_idf[i][0]>max:
                max = tf_idf[i][0]
                doc = tf_idf[i][1]
        return doc
