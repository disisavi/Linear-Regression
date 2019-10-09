from typing import List, Tuple
from random import randint
import sys
import numpy as np


class regressionEngine:
    alpha = 0.00000002  # Convergence control variable
    e = 10  # convergence variable
    lambdareg = 100

    def __init__(self, x, y, maxiterations, test=False):
        self.comparisonerror = sys.maxsize
        self.y = y
        self.x = x
        self.test = test
        self.maxiterations = maxiterations

    def getslice(self, index: int) -> List[int]:
        returnList = [self.x[0][index], self.x[1][index], self.x[2][index]]
        return returnList

    def calculateH(self, thetalist: List, index: int) -> int:
        h = 0
        slice = self.getslice(index)
        for index, theta in enumerate(thetalist):
            h += theta * slice[index]
        return h

    def calculateJ(self, h, y) -> int:
        return (y - h) ** 2

    def calculateJTheta(self, thetalist):
        jtheta = 0
        hlist = []
        for i in range(len(self.y)):
            h = self.calculateH(thetalist, i)
            hlist.append(h)
            jtheta += self.calculateJ(h, self.y[i])

        jtheta = jtheta / (2 * len(self.y))
        return jtheta, hlist

    def convergeDescent(self, newError, oldError, checkErrorGrowth=False):
        errorGettingBigger = False
        if self.test:
            print("\t Diff", newError, oldError, oldError - newError)
        errorDiff = abs(oldError - newError)
        if checkErrorGrowth:
            if errorDiff > self.comparisonerror:
                errorGettingBigger = True
            else:
                self.comparisonerror = newError

        return errorDiff <= self.e or errorGettingBigger

    def getThetaForGD(self, theta, hx, reg):
        if reg:
            theta = theta * (1 - self.alpha * self.lambdareg)
        return theta - self.alpha * hx

    def doGradientDecent(self, regularise=False) -> List[Tuple]:
        self.comparisonerror = sys.maxsize
        iterationList: List = []
        thetaMatrix = [[10000, 10000, 10000]]

        if self.test:
            print("************ Starting gradient descent. :)")
        for thetaList in thetaMatrix:
            for k in range(self.maxiterations):
                if self.test:
                    print("Iteration Number ", k)
                newthetalist = []
                h = [(self.calculateH(thetaList, i) - self.y[i]) for i in range(len(self.y))]
                firstcheckpass = False

                olderror = self.calculateJTheta(thetaList)[0]
                iterationList.append((thetaList, olderror))
                for i in range(len(thetaList)):
                    hx = [h[j] * self.x[i][j] for j in range(len(h))]
                    hx = sum(hx) / len(self.y)
                    theta = thetaList[i]

                    if regularise and firstcheckpass and i != 0:
                        newTheta = self.getThetaForGD(theta, hx, True)
                    else:
                        newTheta = self.getThetaForGD(theta, hx, False)
                        firstcheckpass = True

                    newthetalist.append(newTheta)

                newerror = self.calculateJTheta(newthetalist)[0]

                if self.convergeDescent(newerror, olderror, True):
                    break
                else:
                    if self.test:
                        print("New theta list ", newthetalist)

                    thetaList = newthetalist

        print("Iterations to complete = ", k)
        return iterationList

    def doStochasticGradientDescent(self, alpha=None) -> List[Tuple]:
        iterationList: List = []
        thetalist = [[10000, 10000, 10000]]

        if self.test:
            print("************ Starting gradient descent. :)")

        if alpha is None:
            alpha = self.alpha

        iList = {}  ##Set of previosly generated i values so that we dont accidentally keep repeating SGD on the same set
        for theta in thetalist:
            for k in range(self.maxiterations):

                while True:
                    i = randint(0, len(self.y) - 1)
                    if i not in iList:
                        break
                h = self.calculateH(theta, i) - self.y[i]
                newThetaList = []
                olderror = self.calculateJTheta(theta)[0]
                iterationList.append((theta, olderror))
                for j in range(len(theta)):
                    hx = h * self.x[j][i]
                    newTheta = theta[j] - alpha * hx
                    newThetaList.append(newTheta)

                newerror = self.calculateJTheta(newThetaList)[0]

                if self.convergeDescent(newerror, olderror):
                    break
                else:
                    if self.test:
                        print("New theta list ", newThetaList)

                    theta = newThetaList

        print("Iterations to complete = ", k)
        return iterationList

    def doClosedSol(self) -> List:
        x = np.array(list(zip(self.x[1], self.x[2])))
        y = np.array(self.y)
        xtranspose = np.transpose(x)
        xinverser = np.linalg.inv(np.dot(xtranspose, x))
        thetamatrix = np.dot(xtranspose, y)
        thetamatrix = np.dot(thetamatrix, xinverser)
        return thetamatrix.tolist()
