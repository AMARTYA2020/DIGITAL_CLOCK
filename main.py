from tkinter import *
from tkinter.ttk import *
from time import strftime


def initial_postion():
    base.update()
    width, height = base.winfo_width(), base.winfo_height()
    base.geometry(f'{width}x{height}+{base.winfo_screenwidth() // 2 - width // 2}+{base.winfo_screenheight() // 2 - height // 2}')


def digitaltime():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(10, digitaltime)


base = Tk()
base.withdraw()
base.title("--DIGITAL CLOCK--")
base.after(0, initial_postion)

label = Label(base, font=("ds_digital", 50), background="green", foreground="yellow")
label.pack(anchor='center')

digitaltime()
base.deiconify()
base.mainloop()
