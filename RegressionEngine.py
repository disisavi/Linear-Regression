from typing import List


class regressionEngine:

    def __init__(self, x, y, maxiterations, test=False):
        self.y = y
        self.x = x
        self.test = test
        self.maxiterations = maxiterations

    def getslice(self, index: int) -> List[int]:
        returnList = [self.x[0][index], self.x[1][index], self.x[2][index]]
        if self.test:
            print("For index {}, slice is {}".format(index, returnList))
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
            if self.test:
                print("For iteration {}, H = {} and J = {}".format(i, h, jtheta[i]))

        jtheta = sum(jtheta)
        print("Jtheta = ", jtheta)
        jtheta = jtheta / (2 * len(self.y))
        return jtheta, hlist

    def doGradientDecent(self):
        thetalist = [[1000, 1000, 1000]]
        # thetalist.append([[0, 0, 0]])

        alpha = 1
        for theta in thetalist:
            for k in range(self.maxiterations):
                newthetalist = []
                h = [(self.calculateH(theta, i) - self.y[i]) for i in range(len(self.y))]
                for i in range(len(theta)):
                    hx = [h[j] * self.x[i][j] for j in range(len(h))]
                    hx = sum(hx) / len(self.y)
                    print("cham ", hx)
                    newthetalist.append(theta[i] - alpha * hx)

                print("iteration {", k, "}\n\t New Theta = ", self.calculateJTheta(newthetalist)[0], "\n\tDiff = ",
                      self.calculateJTheta(newthetalist)[0] - self.calculateJTheta(theta)[0])
                if abs(self.calculateJTheta(newthetalist)[0] - self.calculateJTheta(theta)[0]) > 1:
                    theta = newthetalist
                else:
                    break
        print(k)
        return newthetalist
