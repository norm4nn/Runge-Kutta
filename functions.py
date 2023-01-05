import math


def f0(x, y):
    return y - x**2
def f0_sol(x):
    return -math.exp(x)+(x**2)+(2*x)+2

def f1(x, y):
    return (x**2)*(y**2)*(math.sin(x))-(2*y)/x

def f1_sol(x):
    return 1/(x**2)*(math.cos(x)+1)
def f2(x, y):
    return math.sin(x)
def f2_sol(x):
    return -math.cos(x)
def f3(x, y):
    return math.sin(x)*math.cos(x)-y*math.cos(x)
def f3_sol(x):
    return math.sin(x)+1/(math.exp(math.sin(x)))-1

functions = [f0, f1, f2, f3]
solutions=[f0_sol,f1_sol,f2_sol,f3_sol]
conditions = [(0, 1), (0, 1), (math.pi/2, 0), (0, 0)]

