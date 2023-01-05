import math


def f0(x, y):
    return y - x**2

def f0_sol(x):
    return -math.exp(x)+(x**2)+(2*x)+2

def f1(x, y):
    return y + x**2

def f1_sol(x):
    return math.e**x - x**2 - 2*x - 2

def f2(x, y):
    return math.sin(x)

def f2_sol(x):
    return -math.cos(x)

def f3(x, y):
    return math.sin(x)*math.cos(x)-y*math.cos(x)

def f3_sol(x):
    return math.sin(x)+1/(math.exp(math.sin(x)))-1

def f4(x, y):
    return x*(y**2)

def f4_sol(x):
    return -(2/((x**2) + 1))


functions = [f0, f1, f2, f3, f4]
solutions=[f0_sol,f1_sol,f2_sol,f3_sol, f4_sol]
conditions = [(0, 1), (-2, math.e**(-2) -2), (math.pi/2, 0), (0, 0), (-5, -(2/26))]

