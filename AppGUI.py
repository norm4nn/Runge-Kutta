import tkinter
import functionChartWindow
import matplotlib

equations = ["y' = y - x^2, y(0) = 1", ]

root = tkinter.Tk()
root.geometry('300x400')
root.title("Select equation")

def runChartWindow(whichEquation):
    functionChartWindow.openNewChart(root, whichEquation.get())


def initApp():


    var = tkinter.IntVar()
    for i, equation in enumerate(equations):
        e = tkinter.Radiobutton(root, text=equation, variable=var, value=i)
        e.pack()

    subimtBtn = tkinter.Button(root, text="Select equation", command=lambda: runChartWindow(var))
    subimtBtn.pack(side=tkinter.BOTTOM, pady=20)

    root.mainloop()