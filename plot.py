import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('doppler_broad.csv')
print(data)

voltage = data['voltage']
time = data['time']
print(voltage, time)

plt.figure('plot')
plt.plot(time, voltage)
plt.xlabel('time (ms)')
plt.ylabel('voltage (V)')
plt.show()

width_time = data['time'][2499] - data['time'][0]
print(width_time)
# width = 0.099959999328 ms

width_frequency = 6834,683 
# width = 6834,683*10**6 hz

df = 6834.683/len(time)
print(df)

freq = []
for punten in range(len(time)):
    data_punten = punten*df 
    freq.append(data_punten)
        
print(freq)











