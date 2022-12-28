import tkinter
import functionChartWindow
import matplotlib

equations = ["y' = y - x^2, y(0) = 1", "y' = e^(-2x) - 2y, y(0) = 0.1", ]

root = tkinter.Tk()
root.geometry('450x500')
root.title("Select equation")

spinnerState = "normal"

def runChartWindow(whichEquation, h, stepAmount, isInf):
    functionChartWindow.openNewChart(root, whichEquation.get(), h.get(), stepAmount.get(), isInf.get())


def toggleNumberOfStepsSpinnerStatus(spinner):
    global spinnerState
    if spinnerState == "normal":
        spinnerState = "disabled"
    else:
        spinnerState = "normal"

    spinner.configure(state=spinnerState)



def initApp():


    var = tkinter.IntVar()
    varLength = tkinter.StringVar()
    varAmount = tkinter.StringVar()
    varIsInf = tkinter.IntVar()
    for i, equation in enumerate(equations):
        e = tkinter.Radiobutton(root, text=equation, variable=var, value=i)
        e.pack()

    subimtBtn = tkinter.Button(root, text="Select equation", command=lambda: runChartWindow(var, varLength, varAmount, varIsInf))
    subimtBtn.pack(side=tkinter.BOTTOM, pady=20)


    firstLine = tkinter.Frame(root)
    tkinter.Label(firstLine, text="Length of the step (h):").pack(side=tkinter.LEFT,   expand=True)
    stepLengthSpinner = tkinter.Spinbox(firstLine, from_=0.01, to=1, value=0.1, textvariable=varLength)
    stepLengthSpinner.pack(side=tkinter.LEFT,   expand=True)
    firstLine.pack(side=tkinter.TOP, pady=20)

    secondLine = tkinter.Frame(root)
    tkinter.Label(secondLine, text="Amount of the steps:").pack(side=tkinter.LEFT, expand=True)
    stepAmountSpinner = tkinter.Spinbox(secondLine, from_=1, to=1000000**3, value=1, textvariable=varAmount, state="normal")
    stepAmountSpinner.pack(side=tkinter.LEFT,  expand=True)
    stepAmountCheckBox = tkinter.Checkbutton(secondLine, text="infinity", variable=varIsInf, command= lambda: toggleNumberOfStepsSpinnerStatus(stepAmountSpinner))
    stepAmountCheckBox.pack(side=tkinter.LEFT, padx=10, expand=True)
    secondLine.pack(side=tkinter.TOP)


    root.mainloop()