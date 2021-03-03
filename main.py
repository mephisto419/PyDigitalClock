from tkinter import *
from tkinter.ttk import *

from time import strftime
from tkinter.ttk import Label

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')  # ('%I:%M:%S %p') for 12h format
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital",80), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()
