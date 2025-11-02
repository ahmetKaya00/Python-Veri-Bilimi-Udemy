import numpy as np
import pandas as pd
from scipy import stats

veri = [4000,4200,4100,50000]
mean_np = np.mean(veri)
mean_pd = pd.Series(veri).mean()
median_np = np.median(veri)
median_pd = pd.Series(veri).median()

print("NumPy Ortalama:",mean_np)
print("Pandas Ortalama:",mean_pd)
print("NumPy Median:",median_np)
print("Pandas Median:",median_pd)

data = [3,4,4,5,5,5,6]
mode_sc = stats.mode(data, keepdims=True)
print("SciPy Mod:", mode_sc.mode[0], " (Tekrar sayısı:",mode_sc.count[0],")")

data2 = [4,8,6,5,3]
mean = np.mean(data2)
var_np = np.var(data2, ddof=1)
print("Ortalama:",mean)
print("Varyans:",var_np)
std_np = np.std(data2,ddof=1)
print("Standart Sapma:",std_np)