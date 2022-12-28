import math


def f0(x, y):
    return y - x**2

def f1(x, y):
    return math.exp(-2*x) - 2*y

functions = [f0, f1]
conditions = [(0, 1), (0, 0.1)]

