# Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# %config InlineBackend.figure_format='retina'
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors.nearest_centroid import NearestCentroid

Axes3D = Axes3D

# Load in the data
# df = pd.read_csv('encuesta_limpio_4.csv', delimiter=';')
df = pd.read_csv('encuesta_internautas_binomiales_menos_desviacion.csv', delimiter=',')

# Standardize the data to have a mean of ~0 and a variance of 1
#X_std = StandardScaler().fit_transform(df)
X_std = df.values
'''
# Create a PCA instance: pca
pca = PCA(n_components=50)
principalComponents = pca.fit_transform(X_std)


# Plot the explained variances
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_ratio_, color='black')
plt.xlabel('PCA features')
plt.ylabel('variance %')
plt.xticks(features)
#plt.show()


# Save components to a DataFrame
PCA_components = pd.DataFrame(principalComponents)


plt.scatter(PCA_components[1], PCA_components[0], alpha=.1, color='black')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()


'''
# Finding accurate clusters
ks = range(1, 30)
inertias = []
for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    
    # Fit model to samples
    #model.fit(PCA_components.iloc[:,:3])
    model.fit(df)
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
plt.plot(ks, inertias, '-o', color='black')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()

'''
model = KMeans(n_clusters=8)
# Fit model to samples
model.fit(df)
print(model.cluster_centers_)

centroids = pd.DataFrame(model.cluster_centers_)
centroids.to_csv('centroids.csv', sep=',')
'''