import tkinter
import matplotlib
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import numpy as np
import AppGUI

delay = 10#miliseconds


def updatePlot(ax, X, FX, canvas, window, i):
    ax.clear()
    x = X[-1]
    fx = FX[-1]
    x += 1
    fx = -2 * x * x#tutaj wyliczanie kolejnego f(x+1)

    X.append(x)
    FX.append(fx)
    ax.set_title("Solution: " + AppGUI.equations[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(X, FX)
    canvas.draw()
    window.after(delay, lambda: updatePlot(ax, X, FX, canvas, window, i))


def rungeKuttaMethod():
    pass


def openNewChart(root, i):
    newWindow = tkinter.Toplevel(root)
    newWindow.geometry("764x512")
    newWindow.title("Chart")

    X = [0]#waruenk poczatkowy
    FX = [0]

    fig = matplotlib.figure.Figure()
    ax = fig.add_subplot()
    ax.plot(X, FX)
    ax.set_title("Solution: " + AppGUI.equations[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    canvas = FigureCanvasTkAgg(fig, newWindow)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=tkinter.TOP)

    newWindow.after(delay, lambda: updatePlot(ax, X, FX, canvas, newWindow, i))
    newWindow.mainloop()
