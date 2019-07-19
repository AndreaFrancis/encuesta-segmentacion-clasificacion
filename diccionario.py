import pandas as pd
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel


df = pd.read_csv('encuesta_internautas_binomiales_menos_desviacion.csv')
columns = list(df.columns.values)
#print(columns)
#print(df.values)
count = 0
texts = []
for i in df.values:
    #print(i)
    count += count
    words = []
    for j, valor in enumerate(i):
        if(valor==1):
            words.append(columns[j])
    texts.append(words)
    if count > 1:
        break

common_dictionary = Dictionary(texts)
common_corpus = [common_dictionary.doc2bow(text) for text in texts]

ldamodel = LdaModel(common_corpus, num_topics=5, id2word = common_dictionary)
print(ldamodel.print_topics(num_topics=5, num_words=5))
