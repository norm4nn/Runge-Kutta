import tkinter

import AppGUI

def openNewChart(root, i):
    newWindow = tkinter.Toplevel(root)
    newWindow.geometry("764x512")
    newWindow.title("Chart")

    newWindow.mainloop()