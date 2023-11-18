import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

data_free = pd.read_csv('doppler_free_new.csv')
# data_free = data_free.iloc[:,3:]
voltage = np.array(data_free['voltage'])
time = np.array(data_free['time'])
print(time,voltage)

# frequency = time*a + b 
# print(frequency)


# plt.figure('plot')
# plt.plot(time, voltage)
# plt.xlabel('time (ms)')
# plt.ylabel('voltage (V)')
# plt.show()






