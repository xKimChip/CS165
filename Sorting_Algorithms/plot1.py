import pandas as pd
import numpy as np
from math import log2, e
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

df_almost = pd.read_csv("results/benchmark2.csv",header=None, names=["Size","Elapsed_Time", "Num_Comp"])
df_random = pd.read_csv("results/benchmark1.csv",header=None, names=["Size","Elapsed_Time", "Num_Comp"])
print(df_almost)

x = df_almost['Size']
y = df_almost['Elapsed_Time']
p = plt.loglog(x, y, '.', markersize = 12)

logx, logy = np.log(x), np.log(y) 

m, b = np.polyfit(logx, logy, 1)

fit = np.poly1d((m, b)) 
expected_logy = fit(logx)

r2 = r2_score(logy, expected_logy)

sort_name = "Imaginary_sort"
perm_name = "Almost_sorted"
fit_p = plt.loglog(x[::len(x)-1], (e ** expected_logy)[::len(y)-1], '--',
label = f'{sort_name} ({perm_name}): {m:0.5} log x + {b:.5}, r^2 = {r2:.5}',
markersize = 6, color = p[-1].get_color())
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') #to put the legend box␣,→outside

p = plt.loglog(x, y, '.', markersize = 12)
fit_p = plt.loglog(x[::len(x)-1], (e ** expected_logy)[::len(y)-1], '--',
label = f'{sort_name} ({perm_name}): {m:0.5} log x + {b:.5}, error = {r2:.5}',
markersize = 6, color = p[-1].get_color())

x2 = df_random['Size']
y2 = df_random['Elapsed_Time']
p_random = plt.loglog(x2, y2, '.', markersize = 12, label= 'Imaginery_sort (Randomomized permutation)')

plt.title("Merge_sort and its best fit line")
plt.xlabel('Input size (n, # of elements)')
plt.ylabel('Elapsed Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')