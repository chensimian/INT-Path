import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
rc('mathtext', default='regular')
#读取数据
try:
    excelFile = './b7.xlsx'
    data = pd.read_excel(excelFile, dtype=str)
except:
    excelFile = './b7.xls'
    data = pd.read_excel(excelFile, dtype=str)
data = pd.DataFrame(data)

time = np.arange(140)
#temp = data['Execution Time']
Swdown = data['Execution Time']
Rn = data['Execution Time']

fig = plt.figure(figsize=(8, 4))  # 调图片大小的
ax = fig.add_subplot(111)

lns1 = ax.plot(time, Swdown, label="Execution Time", c="b", marker="o", markersize=7, markerfacecolor='none')
lns2 = ax.plot(time, Rn, label= "Hierholzer Call Times",c = "r",marker = "^",markersize=7,markerfacecolor='none')
ax2 = ax.twinx()
#lns3 = ax2.plot(time, temp, '-r', label = 'temp')

# added these three lines
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)

ax.grid()
ax.set_xlabel("Time (h)")
ax.set_ylabel(r"Radiation ($MJ\,m^{-2}\,d^{-1}$)")
ax2.set_ylabel(r"Temperature ($^\circ$C)")
ax2.set_ylim(0, 100)
ax.set_ylim(0, 1.8)
plt.show()
#plt.savefig('0.png')