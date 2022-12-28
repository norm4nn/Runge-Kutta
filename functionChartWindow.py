import tkinter
import matplotlib
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import numpy as np
import AppGUI
import functions

delay = 10#miliseconds


def updatePlot(ax, X, FX, canvas, window, i, h, N, isInf, currentStep):
    if(not isInf and currentStep >= N):
        return
    currentStep += 1
    ax.clear()
    fx = FX[-1]
    x = X[-1]
    fx = rungeKuttaMethod(x, fx, h, i)
    x += h
    #tutaj wyliczanie kolejnego f(x+1)

    X.append(x)
    FX.append(fx)
    ax.set_title("Solution: " + AppGUI.equations[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(X, FX)
    canvas.draw()
    window.after(delay, lambda: updatePlot(ax, X, FX, canvas, window, i, h, N, isInf, currentStep))


def rungeKuttaMethod(x, y, h, i):
    k1 = h*functions.functions[i](x,y)
    k2 = h*functions.functions[i](x + h/2,y + k1/2)
    k3 = h*functions.functions[i](x + h/2,y + k2/2)
    k4 = h*functions.functions[i](x + h,y + k3)

    deltaY = (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y + deltaY


def openNewChart(root, i, h, stepAmount, isInf):
    h = float(h)
    stepAmount = int(stepAmount)
    isInf = int(isInf)
    print(isInf)
    newWindow = tkinter.Toplevel(root)
    newWindow.geometry("764x512")
    newWindow.title("Chart")

    X = [functions.conditions[i][0]]#waruenk poczatkowy
    FX = [functions.conditions[i][1]]

    fig = matplotlib.figure.Figure()
    ax = fig.add_subplot()
    ax.plot(X, FX)
    ax.set_title("Solution: " + AppGUI.equations[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    canvas = FigureCanvasTkAgg(fig, newWindow)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=tkinter.TOP)

    newWindow.after(delay, lambda: updatePlot(ax, X, FX, canvas, newWindow, i, h, stepAmount, isInf, 0))
    newWindow.mainloop()
