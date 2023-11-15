import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('doppler_broad.csv')
voltage = data['voltage']
time = data['time']

def peak(tijdlijst, spanninglijst, start, stop):
    y_min = 3.8
    for i in range(len(tijdlijst)):
        if tijdlijst[i] >= start and tijdlijst[i] <= stop:
            if spanninglijst[i] < y_min:
                x_min = tijdlijst[i]
                y_min = spanninglijst[i]
    return x_min

y_max = 3
for i in range(len(voltage)):
    if voltage[i] > y_max:
        y_max = voltage[i]
        x_0 = time[i]
print(x_0, y_max)

new_time = []
new_voltage = []
for j in range(len(time)):
    if time[j] >= x_0:
        new_time.append(time[j])
        new_voltage.append(voltage[j])

plt.figure('plot')
plt.plot(new_time, new_voltage)

plt.xlabel('time (ms)')
plt.ylabel('voltage (V)')
plt.show()

first_peak = peak(new_time, new_voltage, 0.1250, 0.1260)
last_peak = peak(new_time, new_voltage, 0.154, 0.158)

print(first_peak, last_peak)

a = 266.652/(last_peak - first_peak)

b = -72.911 - first_peak*a

freq = []
for x in new_time:
    y = x * a + b
    freq.append(y)
print(freq)

plt.plot(freq, new_voltage)
plt.xlabel('freq (MHz) + 384*10^6 ')
plt.ylabel('voltage (V)')
plt.show()


# print(voltage, time)
# plt.figure('plot')
# plt.plot(time, voltage)
# plt.xlim()
# plt.xlabel('time (ms)')
# plt.ylabel('voltage (V)')
# plt.show()













