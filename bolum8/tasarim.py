import matplotlib.pyplot as plt
import seaborn as sns

print(plt.style.available)

plt.style.use("seaborn-v0_8-bright")

sns.set_theme(style="whitegrid",palette="deep",font_scale=1.1)

df = sns.load_dataset("tips")

sns.boxplot(x="day",y="total_bill",data=df)
plt.title("Gunlere Gore Ortalama Hesap")
plt.show()

sns.set_palette("coolwarm")
sns.barplot(x="day",y="tip",data=df)
plt.title("Renk Paleti: coolwarm")
plt.show()

plt.figure(figsize=(7,5))
sns.barplot(x="day",y="total_bill",hue="sex",data=df,palette="viridis")

plt.title("Gun ve Cinsiyete Gore Ortalama Hesap Miktari",fontsize=13,fontweight="bold")
plt.xlabel("Gun",fontsize=12)
plt.ylabel("Toplam Hesap",fontsize=12)
plt.legend(title="Cinsiyet",loc="upper right")
plt.grid(True,alpha=0.2)
plt.tight_layout()
plt.show()