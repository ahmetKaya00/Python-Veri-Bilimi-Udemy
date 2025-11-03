import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import cross_val_score

data = pd.DataFrame({
    "m2": [80,100,120,150,200,250,300,350],
    "oda":[2,2,3,3,4,5,5,6],
    "fiyat":[250000,310000,400000,460000,620000,730000,800000,910000]
})

x=data[["m2","oda"]]
y=data["fiyat"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("Gerçek Değer:",list(y_test))
print("Tahmin Değer:",list(y_pred))

mae = mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"MAE: {mae}")
print(f"R2 Skoru: {r2}")

scores = cross_val_score(model,x,y,cv=4,scoring="r2")

print("Fold Skorları:", scores)
print("Ortalama R2:",scores.mean())