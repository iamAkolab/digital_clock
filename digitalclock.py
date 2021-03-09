#from module import package

from tkinter import *
from time import strftime

# creates a tinker window
root = Tk()  

# Adds title to tkinter window
root.title("Digital Clock")

# Function used display time on the label
def time():
    string = strftime("%H:%M:%S  %p")
    lbl.config(text = string)
    lbl.after(1000, time)

#styling the label widget which displays the clock
lbl = Label(root, font = ("arial", 160, "bold"), bg = "black", fg = "white")

# pack method in tkinter pcks widgets into rows or columns, 
lbl.pack(anchor="center", fill="both", expand = 1)

# Time function is called
time()

# Runs the application program
mainloop()