import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

print(tips.head())
print(iris.head())

sns.pairplot(iris,hue="species",diag_kind="kde")
plt.suptitle("Iris Veri Seti PairPlot",y=1.02)
plt.show()

corr = tips.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap="coolwarm",linewidths=0.5)
plt.title("Bahsis Verilerinde Korelasyon Haritası")
plt.show()

sns.catplot(x="day",y="total_bill",kind="bar",data=tips,palette="Blues")
plt.title("Gunlere Gore Ortalama Hesap Miktari")
plt.show()

sns.set_palette("coolwarm")
sns.boxplot(x="day",y="tip",data=tips)
plt.title("Renk Paleti Uygulamasi")
plt.show()