import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(42)
grup1 = np.random.normal(70,10,30)
grup2 = np.random.normal(74,10,30)

t,p = stats.ttest_ind(grup1,grup2)
print("t-istatistigi", round(t,3)," | p-degeri:",round(p,4))

grupA = np.random.normal(75,10,30)
grupB = np.random.normal(80,10,30)
grupC = np.random.normal(85,10,30)

f,p = stats.f_oneway(grupA,grupB,grupC)
print("F-İstatistigi:",round(f,3),"| p-degeri:",round(p,4))

veri = pd.DataFrame({
    "Cinsiyet": ["Kadın","Kadın","Erkek","Erkek","Kadın","Erkek","Kadın","Erkek"],
    "Tercih":["A","A","B","B","A","B","A","B"]
})

ct = pd.crosstab(veri["Cinsiyet"],veri["Tercih"])
print(ct)

chi2, p, dof, beklenen = stats.chi2_contingency(ct)
print("Ki-Kare", round(chi2,3), "| p:",round(p,4))