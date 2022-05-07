from Doc_class import Doc
from Docs_class import Docs
from nltk.stem import PorterStemmer
import nltk
# creation files
file1 = Doc("franklin","Franklin_D_Roosevelt’s.txt")
file2 = Doc("ronald","Ronald_Reagan’s.txt")
file3 = Doc("dwight","Dwight_Eisenhower’s.txt")
file4 = Doc("lyndon","Lyndon_B_Johnson’s.txt")
file5 = Doc("kenedy","John_F_Kennedy’s.txt")
stat  = Docs(file1,file2,file3,file4,file5)
word = input("type your word: ")
ps = PorterStemmer()
word = ps.stem(word)
print(stat.doc_hote(word))
print(stat.word_frequency(word))
print(stat.weight(word))
print(stat.tf_idf(word))
print(stat.most_relevant(word))
