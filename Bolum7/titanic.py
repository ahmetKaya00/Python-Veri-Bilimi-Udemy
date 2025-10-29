import pandas as pd

df = pd.read_csv("Titanic.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

print(df["Survived"].value_counts(normalize=True)*100)

print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Survived"].mean())