import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from typing import List

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


def calculateH(thetalist: List, slice) -> int:
    h = 0

    for index, theta in enumerate(thetalist):
        # print(slice[index])
        h += theta * slice[index]

    return h


def calculateJ(h, y) -> int:
    return (y - h) ** 2


def calculateJTheta(x, y, thetalist):
    jtheta = 0
    hlist = []
    for i in range(len(y)):
        h = calculateH(thetalist, [x[0][i], x[1][i], x[2][i]])
        hlist.append(h)
        jtheta += calculateJ(h, y[i])

    jtheta = jtheta / (2 * len(y))
    return jtheta, hlist


def doLinearRegression():
    global x, y
    thetalist = []
    thetalist.append([1000, 1000, 1000])
    # thetalist.append([[0, 0, 0]])

    alpha = -0.001
    for theta in thetalist:
        for k in range(1000):
            newthetalist = []
            h = [(calculateH(theta, [x[0][i], x[1][i], x[2][i]]) - y[i]) for i in range(len(y))]
            for i in range(len(theta)):
                hx = [h[j] * x[i][j] for j in range(len(h))]
                hx = sum(hx) / len(y)
                print("cham ", hx)
                newthetalist.append(theta[i] - alpha * hx)

            print("Tamatar", calculateJTheta(x, y, newthetalist)[0] - calculateJTheta(x, y, theta)[0])
            if abs(calculateJTheta(x, y, newthetalist)[0] - calculateJTheta(x, y, theta)[0]) > 1:
                theta = newthetalist
            else:
                break
    print(k)
    return newthetalist


thetalist = doLinearRegression()
jtheta, hlist = calculateJTheta(x, y, thetalist)
print(jtheta)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x[1], x[2], y, 'blue')
ax.scatter(x[1], x[2], hlist, 'gray')
plt.show()
