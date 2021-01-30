from tkinter import *
from tkinter.ttk import *
from time import strftime

base = Tk()
base.title("--DIGITAL CLOCK--")



def digitaltime():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(2000, digitaltime())


label = Label(base, font=("ds_digital",70),background = "green", foreground = "yellow")
label.pack(anchor='center')

digitaltime()

