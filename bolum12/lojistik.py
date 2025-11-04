import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "puan": [45,50,55,60,65,70,75,80,85,90],
    "gecti_mi":[0,0,0,0,1,1,1,1,1,1]
})

x = data[["puan"]]
y = data["gecti_mi"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print("Tahminler:",y_pred)
print("Doğruluk:",accuracy_score(y_test,y_pred))

print(model.predict_proba(x_test))