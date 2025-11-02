import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import stats
from sklearn.preprocessing import StandardScaler

mu, sigma = 0,1
x = np.linspace(-4,4,1000)
y = norm.pdf(x,mu,sigma)

plt.plot(x,y,color="navy")
plt.title("Standart normal dagilim")
plt.xlabel("Deger")
plt.ylabel("Olasılık Yogunlugu")
plt.grid(True)
plt.show()

np.random.seed(42)
yaslar = np.random.normal(35,10,1000)
plt.hist(yaslar,bins=30,density=True,alpha=0.6,color="skyblue")
plt.axvline(np.mean(yaslar),color="red",linestyle="--",label="Ortalama")
plt.legend()
plt.title("Yas Dagilim")
plt.show()


yas_ornek = 50
z = (yas_ornek - np.mean(yaslar)) / np.std(yaslar)
print("Z-Score:",round(z,2))

scaler = StandardScaler()
yas_z = scaler.fit_transform(yaslar.reshape(-1,1))
print("İlk 5 Z-Score:", yas_z[:5].flatten())

p = norm.cdf(1.96)
print("Z=1.96 için alan:",p)
print("Sağ Kuyruk Olasılığı:",1-p)

z_obs = 2.1
p_degeri = 2 * (1 - norm.cdf(abs(z_obs)))
print("Z-Score:",z_obs, " -> P-Değeri:",round(p_degeri,4))