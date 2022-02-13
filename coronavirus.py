import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import csv

date, positive, deaths, Total_Tests = [], [], [], []
with open('covid.csv') as f:
    reader = csv.DictReader(f)
    reader = reversed(list(reader))
    for data in reader:
        date.append(data['Date'])
        positive.append(int(data['Positive']))
        deaths.append(int(data['Deaths']))
        Total_Tests.append(int(data['Total Tests']))

# Data for plotting

fig, ax = plt.subplots()
ax.plot(date, positive)
ax.plot(date, deaths)
ax.plot(date, Total_Tests)

ax.set(xlabel='x', ylabel='y',
       )
ax.grid()

plt.show()
