import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "m2": [50,60,70,80,100,120,150,200,250,300],
    "fiyat":[150000,180000,200000,230000,280000,320000,400000,500000,620000,750000]
})

x = data[["m2"]]
y=data["fiyat"]

model = LinearRegression()
model.fit(x,y)

print("Katsayı:",model.coef_[0])
print("Kesişim:",model.intercept_)

tahmin = model.predict([[180]])
print("180 m2 ev için tahmini fiyat:",tahmin[0])

y_pred = model.predict(x)
mae = mean_absolute_error(y,y_pred)
r2 = r2_score(y,y_pred)

print(mae)
print(r2)

plt.scatter(x,y,color="blue", label= "Gerçek Veriler")
plt.plot(x,y_pred,color="red",label="Regresyon Dogrusu")
plt.xlabel("Metrekare")
plt.ylabel("Fiyat")
plt.title("Dogrusal Regresyon")
plt.legend()
plt.show()
