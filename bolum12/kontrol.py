from sklearn.metrics import classification_report,roc_auc_score
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x,y = load_breast_cancer(return_X_y=True)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model = LogisticRegression(max_iter=5000)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print(classification_report(y_test,y_pred))
print("ROC-AUC",roc_auc_score(y_test,model.predict_log_proba(x_test)[:,1]))
