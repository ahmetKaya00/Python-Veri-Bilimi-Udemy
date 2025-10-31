from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
import pandas as pd, numpy as np
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


data = pd.DataFrame({"yas":[22,np.nan,35,29],"maas":[4000,5200,np.nan,5900]})
imputer = SimpleImputer(strategy="median")
filled = imputer.fit_transform(data)
print(filled)

knn = KNNImputer(n_neighbors=3,weights="distance")
filled_knn = knn.fit_transform(data)
print(filled_knn)

pipe = Pipeline([
    ("imputer",SimpleImputer(strategy="median")),
    ("model",LinearRegression())
])