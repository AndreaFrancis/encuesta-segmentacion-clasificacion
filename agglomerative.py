from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd

df = pd.read_csv('encuesta_internautas_binomiales_menos_desviacion.csv', delimiter=',')
X = df.values

model = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
model.fit(X)
labels = model.labels_
print(labels)