from typing import List
import sys


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
        # if self.test:
        #     print("For index {}, slice is {}".format(index, returnList))
        return returnList

    def calculateH(self, thetalist: List, index: int) -> int:
        h = 0
        slice = self.getslice(index)
        for index, theta in enumerate(thetalist):
            # print(slice[index])
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
            # if self.test:
            #     print("For iteration {}, H = {} and J = {}".format(i, h, jtheta[i]))

        jtheta = sum(jtheta)
        # print("Jtheta = ", jtheta)
        jtheta = jtheta / (2 * len(self.y))
        return jtheta, hlist

    def doGradientDecent(self) -> List[int]:
        thetalist = [[100, 100, 100]]
        # thetalist.append([[0, 0, 0]])
        if self.test:
            print("************ Starting gradient descent. :)")
        for theta in thetalist:
            for k in range(self.maxiterations):
                # todo
                # 1. Allow multiple theta's to be initialised from the start and then compare
                # the final result among all of them to check we reached True Minima
                if self.test:
                    print("Iteration Number ", k)
                newthetalist = []
                h = [(self.calculateH(theta, i) - self.y[i]) for i in range(len(self.y))]
                # if self.test:
                #     print("The hi - yi = ", h)

                olderror = self.calculateJTheta(theta)[0]
                for i in range(len(theta)):
                    hx = [h[j] * self.x[i][j] for j in range(len(h))]
                    hx = sum(hx) / len(self.y)
                    newTheta = theta[i] - self.alpha * hx
                    # if self.test:
                    #     print("\tNew HX ", hx)
                    #     print("NewTheta = ", newTheta)
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
