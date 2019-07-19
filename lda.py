from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary

common_dictionary = Dictionary(common_texts)
print(common_texts)
print(common_dictionary)