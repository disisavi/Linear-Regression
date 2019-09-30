from typing import List


class regressionEngine:
    alpha = 0.00000002  # Convergence control variable
    e = 10  # convergence variable

    def __init__(self, x, y, maxiterations, test=False):
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
        jtheta = []
        hlist = []
        for i in range(len(self.y)):
            h = self.calculateH(thetalist, i)
            hlist.append(h)
            jtheta.append(self.calculateJ(h, self.y[i]))

        jtheta = sum(jtheta)
        jtheta = jtheta / (2 * len(self.y))
        return jtheta, hlist

    def doGradientDecent(self) -> List[int]:
        thetalist = [[1000, 1000, 1000]]

        if self.test:
            print("************ Starting gradient descent. :)")
        for theta in thetalist:
            for k in range(self.maxiterations):
                if self.test:
                    print("Iteration Number ", k)
                newthetalist = []
                h = [(self.calculateH(theta, i) - self.y[i]) for i in range(len(self.y))]

                olderror = self.calculateJTheta(theta)[0]
                for i in range(len(theta)):
                    hx = [h[j] * self.x[i][j] for j in range(len(h))]
                    hx = sum(hx) / len(self.y)
                    newTheta = theta[i] - self.alpha * hx
                    newthetalist.append(newTheta)

                newerror = self.calculateJTheta(newthetalist)[0]
                if self.test:
                    print("\t Diff", newerror, olderror, olderror - newerror)
                    print("Thetalist ", newthetalist)
                errorDiff = olderror - newerror

                if errorDiff > self.e:
                    theta = newthetalist
                else:
                    break

        print("K = ", k)
        return newthetalist

# todo
# 1. Allow multiple theta's to be initialised from the start and then compare
# the final result among all of them to check we reached True Minima
