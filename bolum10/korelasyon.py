import pandas as pd
import numpy as np
from scipy.stats import pearsonr,spearmanr
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
veri = pd.DataFrame({
    "yas": np.random.randint(20,60,50),
    "maas": np.random.randint(3000,10000,50)
})
print(veri.head())

corr = veri["yas"].corr(veri["maas"],method="pearson")
print("Pearson Korelasyon Katsayısı:",round(corr,3))

r,p = pearsonr(veri["yas"],veri["maas"])
print("Pearson r:",round(r,3), " | P-Değeri:",round(p,4))

x = veri[["yas"]]
y = veri["maas"]

model = LinearRegression()
model.fit(x,y)

print("Eğim:",model.coef_[0])
print("Sabit", model.intercept_)

veri2 = pd.DataFrame({
    "reklam": [5,10,15,20,25,30],
    "satis": [65,80,100,120,150,170]
})
sns.regplot(data=veri2, x="reklam",y="satis",color="green")
plt.title("Reklam Harcamasi ve Satis Iliskisi")
plt.show()

r,p = pearsonr(veri2["reklam"], veri2["satis"])
print("Korelasyon Katsayısı:",r)
print("P-Deferi:",p)