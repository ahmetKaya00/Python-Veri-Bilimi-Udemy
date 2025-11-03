import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "m2": [80,100,150,200],
    "oda": [2,3,3,4],
    "fiyat": [250000,310000,460000,620000]
})

x = df[["m2","oda"]]
y = df["fiyat"]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

model = LinearRegression()
model.fit(x_scaled,y)

y_pred = model.predict(x_scaled)
print(y_pred)