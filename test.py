from RegressionEngine import regressionEngine

x = [[1, 1, 1], [1, 100, 1000], [1, 100, 1000]]
y = [6, 501, 5001]

engine = regressionEngine(x, y, 10, True)
print(engine.calculateH([1, 2, 3], 1))
print(engine.calculateJTheta([1, 2, 3]))
