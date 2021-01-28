import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Aakash's Clock")
root.resizable(0,0)

def Time():
    start = strftime('%H:%M:%S %p')
    label.config(text=start)
    label.after(1000, Time)


label = Label(root, font=("Times new roman", 50, 'bold'), foreground='cyan',background='black')
label.pack(anchor='center')
Time()

root.mainloop()