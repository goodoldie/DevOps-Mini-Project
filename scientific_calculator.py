from tkinter import *  #import this module for GUI
import math as m       #import this for all mathematical functions
root=Tk
root.title("Scientific DevOps Calculator")
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0, columnspan=5, padx=10,pady=15)

def click(to_print):
    old=e.get()
    e.delete(0, END)           #delete everything on screen
    e.insert(0, old+to_print)  #to print num positions correctly
    return

def clear():
    e.delete(0, END)
    return

def bkspace():
    current=e.get()
    length=len(current)-1
    e.delete(length, END)




root.mainloop()
