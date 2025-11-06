from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd

iris = load_iris()
x = iris.data
y = iris.target

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scaled)

df_pca = pd.DataFrame({
    "PC1": x_pca[:,0],
    "PC2": x_pca[:,1],
    "label": y
})

plt.scatter(df_pca["PC1"],df_pca["PC2"],c=y,cmap="viridis")
plt.xlabel("1. Temel Bileşen")
plt.ylabel("2. Temel Bilesen")
plt.title("PCA ile 2 Boyutlu Gorsellestirme")
plt.show()