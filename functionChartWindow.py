import tkinter
import matplotlib
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import numpy as np
from screeninfo import get_monitors

import AppGUI
import functions

delay = 400#miliseconds


def updatePlot(ax, X, FX, canvas, window, i, stepAmount, runga_step):
    if(runga_step<=0.001):
        return
    X = functions.conditions[i][0]  # waruenk poczatkowy
    FX = functions.conditions[i][1]

    # rozwiazanie wayliczone
    sol_x = calculate_solution(stepAmount, i, 0.01, X)[0]  # stepamount przedział
    sol_y = calculate_solution(stepAmount, i, 0.01, X)[1]

    runga_x = calculate_runge_kutta(runga_step, i, stepAmount, X, FX)[0]
    runga_y = calculate_runge_kutta(runga_step, i, stepAmount, X, FX)[1]

    ax.clear()
    ax.set_title("Solution: " + AppGUI.equations[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.scatter(runga_x, runga_y, color='r')
    ax.plot(sol_x, sol_y, color='g')
    ax.set_ylim([-5, 5])
    runga_step/=1.25

    print("licze")


    canvas.draw()
    window.after(delay, lambda: updatePlot(ax, X, FX, canvas, window, i,stepAmount,runga_step))


def rungeKuttaMethod(x, y, h, i):
    k1 = h*functions.functions[i](x,y)
    k2 = h*functions.functions[i](x + h/2,y + k1/2)
    k3 = h*functions.functions[i](x + h/2,y + k2/2)
    k4 = h*functions.functions[i](x + h,y + k3)

    deltaY = (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y + deltaY

def calculate_runge_kutta(step,function_number,number_of_steps,start_x,start_y):
    fx = start_y
    x = start_x
    x_list=[]
    y_list=[]

    while x <= number_of_steps:
        x_list.append(x)
        current_y=rungeKuttaMethod(x,fx,step,function_number)
        y_list.append(current_y)
        fx=current_y
        x += step

    return x_list, y_list

def calculate_solution(number_of_steps,function_number,step,start_x):
    fx=[]
    x=[]
    current_x=start_x
    while current_x<=number_of_steps:
        x.append(current_x)
        fx.append(functions.solutions[function_number](current_x))
        # print(functions.solutions[function_number](current_x))
        current_x+=step

    return x, fx

def cm_to_inch(value):
    return value/2.54

def openNewChart(root, i, stepAmount,runga_step):
    # h = float(h)
    stepAmount = int(stepAmount)
    newWindow = tkinter.Toplevel(root)



    newWindow.geometry("1280x720")
    newWindow.title("Chart")
    screen_width = root.winfo_screenmmwidth()//10
    screen_height = root.winfo_screenmmheight()//10

    screen_height//=1.5
    screen_width//=1.5

    print(screen_width)
    print(screen_height)


    X = functions.conditions[i][0]#waruenk poczatkowy
    FX = functions.conditions[i][1]

    # rozwiazanie wayliczone
    sol_x = calculate_solution(stepAmount, i,0.01,X)[0]#stepamount przedział
    sol_y = calculate_solution(stepAmount, i,0.01,X)[1]

    runga_step = 1
    runga_x = calculate_runge_kutta(runga_step,i,stepAmount,X,FX)[0]
    runga_y = calculate_runge_kutta(runga_step,i,stepAmount,X,FX)[1]




    fig = matplotlib.figure.Figure(figsize=(cm_to_inch(screen_width),cm_to_inch(screen_height)))
    ax = fig.add_subplot()

    ax.scatter(runga_x, runga_y,color='r')
    ax.plot(sol_x, sol_y, color='g')
    ax.set_title("Solution: " + AppGUI.equations[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim([-5, 5])
    canvas = FigureCanvasTkAgg(fig, newWindow)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=tkinter.TOP)
    newWindow.after(delay, lambda: updatePlot(ax, X, FX, canvas, newWindow, i, stepAmount, runga_step))
    newWindow.mainloop()
