from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay
from sklearn.linear_model import LogisticRegression



x,y = load_iris(return_X_y=True)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

tree = DecisionTreeClassifier(max_depth=3,random_state=42)
tree.fit(x_train,y_train)

y_pred = tree.predict(x_test)
print("doğruluk:",accuracy_score(y_test,y_pred))

rf = RandomForestClassifier(n_estimators=100,random_state=42)
rf.fit(x_train,y_train)

print("Accuary:",rf.score(x_test,y_test))

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

print("KNN Accuary:",knn.score(x_test,y_test))

cm = confusion_matrix(y_test,y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.show()
model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
RocCurveDisplay.from_estimator(model,x_test,y_test)
plt.title("ROC Egrisi")
plt.show