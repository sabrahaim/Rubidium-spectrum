import pandas as pd
import csv
import matplotlib.pyplot as plt
    
data = pd.read_csv('doppler_broad.csv')
print(data)

voltage = data['voltage']
time = data['time']
print(voltage, time)

plt.plot(time, voltage)
plt.xlabel('time (ms)')
plt.ylabel('voltage (V)')
plt.show()



