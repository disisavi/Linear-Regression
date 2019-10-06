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

iterationThetaListGD = engine.doGradientDecent()
errorListGD = list(zip(*iterationThetaListGD))[1]
plt.plot(errorListGD, 'RED', label='GD')
plt.legend()
plt.show()

iterationThetaListSGD = engine.doStochasticGradientDescent()
errorListSGD = list(zip(*iterationThetaListSGD))[1]
plt.plot(errorListSGD, 'BLUE', label='Stochastic GD')
plt.legend()
plt.show()

iterationThetaListL2GD = engine.doGradientDecent(True)
errorListL2GD = list(zip(*iterationThetaListL2GD))[1]
plt.plot(errorListL2GD, 'Green', label='L2')
plt.legend()
plt.show()

totalLength = len(y) - 1
testLenght = round(totalLength * 2 / 3)

thetalist = engine.doClosedSol()
thetalist.insert(0, 121)
jtheta, hlist = engine.calculateJTheta(thetalist)
print("The Lw for Closed sol is\t -- ", jtheta)

xtrain = []
xtrain.append([x[0][i] for i in range(testLenght)])
xtrain.append([x[1][i] for i in range(testLenght)])
xtrain.append([x[2][i] for i in range(testLenght)])
ytest = [y[i] for i in range(testLenght)]

xpredict = []
xpredict.append([x[0][i] for i in range(testLenght, totalLength - 1)])
xpredict.append([x[1][i] for i in range(testLenght, totalLength - 1)])
xpredict.append([x[2][i] for i in range(testLenght, totalLength - 1)])
ypredict = [y[i] for i in range(testLenght, totalLength - 1)]

trainEngine = regressionEngine(xtrain, ytest, 1000, False)
predictEngine = regressionEngine(xpredict, ypredict, 1000, False)

iterationThetaListGD = trainEngine.doGradientDecent()
thetalist = iterationThetaListGD[len(iterationThetaListGD) - 1][0]

jtheta, hlist = trainEngine.calculateJTheta(thetalist)
print("The Lw for Training data for GD -- ", jtheta)

jtheta, hlist = predictEngine.calculateJTheta(thetalist)
print("The Lw for Test data for GD \t-- ", jtheta)

iterationThetaListSGD = trainEngine.doStochasticGradientDescent()
thetalist = iterationThetaListSGD[len(iterationThetaListSGD) - 1][0]

jtheta, hlist = trainEngine.calculateJTheta(thetalist)
print("The Lw for Training data for SGD -- ", jtheta)

jtheta, hlist = predictEngine.calculateJTheta(thetalist)
print("The Lw for Test data for SGD \t -- ", jtheta)

iterationThetaListL2GD = trainEngine.doGradientDecent(True)
thetalist = iterationThetaListL2GD[len(iterationThetaListL2GD) - 1][0]

jtheta, hlist = trainEngine.calculateJTheta(thetalist)
print("The Lw for Training data for L2GD -- ", jtheta)

jtheta, hlist = predictEngine.calculateJTheta(thetalist)
print("The Lw for Test data for L2GD \t  --  ", jtheta)
