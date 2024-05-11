import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('results/hybridbend.csv', sep=',')
#df2 = pd.read_csv('results/shell_sortbench.csv', sep=',')

# Assuming 'Array Size' and 'Time (ns)' are columns in your CSV
# and you want to plot these for each algorithm
algorithms = df['Algorithm'].unique()
#algorithms2 = df2['Algorithm'].unique()
#fig, ax = plt.subplots()



plt.figure(figsize=(10, 6))
#subset = df2[df2['Algorithm'] == "shell_sort2"]
#logx, logy = np.log2(subset['Array Size']),  np.log2(subset['Time (ns)'])
#m, b = np.polyfit(logx, logy, 1)
#plt.loglog(subset['Array Size'], subset['Time (ns)'], label=f'{"shell_sort2"} ~ {round(m,5)} log N + {round(b,5)}', marker='o')


for algorithm in algorithms: 
    #if (algorithm == "shell_sort2"):
    #    subset = df2[df2['Algorithm'] == "shell_sort2"]
    #    logx, logy = np.log2(subset['Array Size']),  np.log2(subset['Time (ns)'])
    #    m, b = np.polyfit(logx, logy, 1)
    #    plt.loglog(subset['Array Size'], subset['Time (ns)'], label=f'{"shell_sort2"} ~ {round(m,5)} log N + {round(b,5)}', marker='o')
    #    continue
    subset = df[df['Algorithm'] == algorithm]
    logx, logy = np.log2(subset['Array Size']),  np.log2(subset['Time (ns)'])
    m, b = np.polyfit(logx, logy, 1)
    plt.loglog(subset['Array Size'], subset['Time (ns)'], label=f'{algorithm} ~ {round(m,5)} log N + {round(b,5)}', marker='o')

plt.legend()
plt.title('Log-Log Plot of Sorting Algorithm Performance')
plt.xlabel('log N')
plt.ylabel('log T(N) (seconds)')
plt.xscale('log',base=2)
plt.yscale('log',base=2)
plt.savefig('Hybrid test.png')
