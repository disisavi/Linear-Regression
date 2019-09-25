import csv
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
from typing import List

x:List[List[int]] = []
y:List[int] = []

for __i in range(3):
    x.append([])

with open('ex1data2.txt') as dataFile:
    data = csv.reader(dataFile)
    for row in data:
        x[0].append(1)
        x[1].append(int(row[0],10))
        x[2].append(int(row[1],10))
        y.append(int(row[2],10))


def calculateH(thetalist:List, slice) -> int : 
    h = 0

    for index,theta in enumerate(thetalist):
        # print(slice[index])
        h +=  theta*slice[index]
        
    return h


def calculateJ(h, y) -> int:
    return (y-h)**2

def calculateJTheta(x,y,thetalist) -> int:
    jtheta = 0

    for i in range(len(y)):
        jtheta += calculateJ(calculateH(thetalist,[x[0][i], x[1][i],x[2][i]]),y[i])

    jtheta = jtheta/(2*len(y))
    return(jtheta)






theta = [2,100,100]

print(calculateJTheta(x,y,theta))
