import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pd.DataFrame({
    "m2": [80,100,120,150,200,250,300,350],
    "oda": [2,2,3,3,4,5,5,6],
    "fiyat": [250000,310000,400000,460000,620000,730000,800000,910000]
})

x = df[["m2","oda"]]
y = df["fiyat"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)

pipe = Pipeline([
    ("scaler",StandardScaler()),
    ("model",LinearRegression())
])

pipe.fit(x_train,y_train)

y_pred = pipe.predict(x_test)
print("Tahminler:",y_pred)