import tkinter
import functionChartWindow
import matplotlib

equations = ["y' = x-y-4, y(-2) = 0.39",
             "y' = y + x^2, y(-2) = e^(-2) - 2",
             "y' = sin(x), y(pi/2) = 0",
             "y' = sin(x)cos(x)-ycos(x), y(0) = 0",
             "y' = y^2 * x, y(-5) = -2/26"]

root = tkinter.Tk()
root.geometry('450x500')
root.title("Runge-Kutta")

spinnerState = "normal"

def runChartWindow(whichEquation,stepAmount, starting_step):
    functionChartWindow.openNewChart(root, whichEquation.get(), stepAmount.get(), starting_step.get())


def toggleNumberOfStepsSpinnerStatus(spinner):
    global spinnerState
    if spinnerState == "normal":
        spinnerState = "disabled"
    else:
        spinnerState = "normal"

    spinner.configure(state=spinnerState)



def initApp():
    varWhich = tkinter.IntVar()
    varLength = tkinter.StringVar()
    varAmount = tkinter.StringVar()

    for i, equation in enumerate(equations):
        e = tkinter.Radiobutton(root, text=equation, variable=varWhich, value=i)
        e.pack()


    firstLine = tkinter.Frame(root)
    tkinter.Label(firstLine, text="Length of runge-kutta the step (h):").pack(side=tkinter.LEFT,   expand=True)
    stepLengthSpinner = tkinter.Spinbox(firstLine, from_=1, to=10, value=3, textvariable=varLength)
    stepLengthSpinner.pack(side=tkinter.LEFT,   expand=True)
    firstLine.pack(side=tkinter.TOP, pady=20)




    secondLine = tkinter.Frame(root)
    tkinter.Label(secondLine, text="Przedział (warunek początkowy,wybrana wartość) :").pack(side=tkinter.LEFT, expand=True)
    stepAmountSpinner = tkinter.Spinbox(secondLine, from_=1, to=100, value=10, textvariable=varAmount, state="normal")
    stepAmountSpinner.pack(side=tkinter.LEFT,  expand=True)

    secondLine.pack(side=tkinter.TOP)



    subimtBtn = tkinter.Button(root, text="Select equation",
                               command=lambda: runChartWindow(varWhich, varAmount,varLength))
    subimtBtn.pack(side=tkinter.BOTTOM, pady=20)

    root.mainloop()