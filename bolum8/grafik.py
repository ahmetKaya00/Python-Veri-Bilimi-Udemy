import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,25,30,35]

plt.plot(x,y)
plt.show()

aylar = ["Ocak","Şubat","Mart","Nisan","Mayıs"]
satislar = [120,150,170,160,185]

plt.plot(aylar,satislar,color="#027A94",linestyle="--",marker="o",linewidth=2)
plt.title("Aylik Satis Grafigi")
plt.xlabel("Aylar")
plt.ylabel("Satis Miktari")
plt.grid(True)
plt.show()

plt.bar(aylar,satislar,color="#20BAD1",edgecolor="black")
plt.title("Aylik Satislar")
plt.xlabel("Ay")
plt.ylabel("Satis")
plt.show()

yaslar = [22,23,24,25,25,26,26,27,28,29,30,30,31,33,35,38,40]
plt.hist(yaslar,bins=5, color="#7CD2DF",edgecolor="black")
plt.title("Yas Dagilimi")
plt.xlabel("Yas Araligi")
plt.ylabel("Kisi Sayisi")
plt.show()

kategoriler = ["Web","Mobil","Masaüstü"]
oranlar=[50,35,15]
plt.pie(oranlar,labels=kategoriler,autopct="%1.1f%%",startangle=90,colors=["#027A94","#20BAD1","#7CD2DF"])
plt.title("Platform Kullanim Dagilimi")
plt.show()

gelir = [25,30,35,40,45,50,55,60]
harcama = [12,15,20,25,28,32,36,40]

plt.scatter(gelir,harcama, color="#027A94",s=80,alpha=0.8)
plt.title("Gelir - Harcama Iliskisi")
plt.xlabel("Gelir")
plt.ylabel("Harcama")
plt.savefig("gelir_grafik.png",dpi=300,bbox_inches="tight")
plt.show()