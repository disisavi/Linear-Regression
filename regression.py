import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from typing import List
from RegressionEngine import regressionEngine

x: List[List[int]] = []
y: List[int] = []

for __i in range(3):
    x.append([])

with open('ex1data2.txt') as dataFile:
    data = csv.reader(dataFile)
    for row in data:
        x[0].append(1)
        x[1].append(int(row[0], 10))
        x[2].append(int(row[1], 10))
        y.append(int(row[2], 10))

engine = regressionEngine(x, y, 1000, False)

thetalist = engine.doGradientDecent()
print("THe theta is ", thetalist)

jtheta, hlist = engine.calculateJTheta(thetalist)
print("The error is  ", jtheta)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x[1], x[2], y, 'blue')
ax.scatter(x[1], x[2], hlist, 'gray')
plt.show()
