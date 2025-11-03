import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

rng = np.random.RandomState(42)
m2 = rng.normal(100,20,50)
oda = rng.randint(1,5,50)
fiyat = 1000*m2 + 20000*oda+rng.normal(0,15000,50)

df = pd.DataFrame({"m2":m2,"oda":oda,"fiyat":fiyat})

x = df[["m2","oda"]]
y = df["fiyat"]

model = LinearRegression()
model.fit(x,y)

print("Katsayılar:",model.coef_)
print("Kesişim:",model.intercept_)

df["etiket"] = (df["fiyat"]>df["fiyat"].median()).astype(int)
logmodel = LogisticRegression()
logmodel.fit(x,df["etiket"])

print("Logistic Katsayılar:",logmodel.coef_)

kmeans = KMeans(n_clusters=2,n_init='auto')
kmeans.fit(x)

df["cluster"] = kmeans.labels_
plt.scatter(df["m2"],df["oda"],c=df["cluster"],cmap="viridis")
plt.xlabel("Metrekare")
plt.ylabel("Oda Sayısı")
plt.title("Kmeans Kumeleme")
plt.show()