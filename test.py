from RegressionEngine import regressionEngine

x = [[1, 1, 1], [1, 100, 1000], [1, 100, 1000]]
y = [6, 501, 5001]

engine = regressionEngine(x, y, 20, True)
# x1 = engine.calculateH([1000, 1000, 1000], 0)
# x2 = engine.calculateH([1000, 1000, 1000], 1)
# x3 = engine.calculateH([1000, 1000, 1000], 2)
#
# print(x1-y[0])
# print(x2-y[1])
# print(x3-y[2])


# print(engine.calculateH([1, 2, 3], 1))
# print(engine.calculateJTheta([1, 2, 3]))
engine.doGradientDecent()
