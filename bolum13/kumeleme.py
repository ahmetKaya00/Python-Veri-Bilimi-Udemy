import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from scipy.cluster.hierarchy import dendrogram,linkage

x, _ = make_blobs(n_samples=200,centers=4,cluster_std=1.2,random_state=42)

plt.scatter(x[:,0],x[:,1])
plt.title("Veri Dagilimi")
plt.show()

kmeans = KMeans(n_clusters=4,random_state=42)
kmeans.fit(x)

y_kmeans = kmeans.predict(x)

plt.scatter(x[:,0],x[:,1], c=y_kmeans, cmap="viridis")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=200,c="red",marker="X",label="Merkezler")
plt.legend()
plt.title("K-Means Kumeleme Sonucu")
plt.show()

inertia_values = []
for k in range(1,10):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(x)
    inertia_values.append(model.inertia_)

plt.plot(range(1,10),inertia_values,marker="o")
plt.xlabel("Kume Sayisi")
plt.ylabel("Inertia")
plt.title("Elbow Yonetimi")
plt.show()

dbscan = DBSCAN(eps=1.5,min_samples=5)
y_dbscan = dbscan.fit_predict(x)

plt.scatter(x[:,0],x[:,1],c=y_dbscan,cmap="plasma")
plt.title("DBSCAN Kumeleme")
plt.show()

linked = linkage(x,method="ward")
dendrogram(linked)
plt.title("Hiyerarsik Kumeleme")
plt.show()