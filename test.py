from Doc_class import Doc
from Docs_class import Docs
file1 = Doc("franklin","Franklin_D_Roosevelt’s.txt")
file2 = Doc("ronald","Ronald_Reagan’s.txt")
file3 = Doc("dwight","Dwight_Eisenhower’s.txt")
file4 = Doc("lyndon","Lyndon_B_Johnson’s.txt")
file5 = Doc("kenedy","John_F_Kennedy’s.txt")
stat  = Docs(file1,file2,file3,file4,file5)
#print(stat.doc_per("enemy"))
print(stat.word_frequency("the"))
#print(stat.poids("the"))
print(stat.tf_idf("the"))
print(stat.most_relevant("the"))