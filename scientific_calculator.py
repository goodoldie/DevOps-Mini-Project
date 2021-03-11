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

def evaluate():
    ans=e.get()
    ans=eval(ans)
    e.delete(0, END)
    e.insert(0, ans)

def sc(event):
    key=event.widget
    text=key['text']
    no=e.get()
    result=''
    if text=='deg':
        result=str(m.degrees(float(no)))
    if text=='sin':
        result=str(m.sin(float(no)))
    if text=='cos':
        result=str(m.cos(float(no)))
    if text=='tan':
        result=str(m.tan(float(no)))
    if text=='lg':
        result=str(m.log10(float(no)))
    if text=='ln':
        result=str(m.log(float(no)))
    if text=='Sqrt':
        result=str(m.sqrt(float(no)))
    if text=='x!':
        result=str(m.factorial(float(no)))
    if text=='1/x':
        result=str(1/(float(no)))
    if text=='pi':
        if no=="":
            result=str(m.pi)
        else:
            result=str(float(no) * m.pi)
    if text=='e':
        if no=="":
            result=str(m.e)
        else:
            result=str(m.e**float(no))



root.mainloop()
