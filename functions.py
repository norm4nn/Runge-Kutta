import math


def f0(x, y):
    return y - x**2

def f1(x, y):
    return math.exp(-2*x) - 2*y

def f2(x, y):
    return math.sin(x)

def f3(x, y):
    return -y**2/x

functions = [f0, f1, f2, f3]
conditions = [(0, 1), (0, 0.1), (math.pi/2, 0), (1, 1)]

