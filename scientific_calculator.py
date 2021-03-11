from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific DevOps Calculator")
root.configure(background="Powder blue")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

#Calculator Classes and methods

class Calc:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.ip_val = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self,num):
        self.result = False
        first_num = txtDisplay.get()
        second_num = str(num)

        if self.ip_val:
            self.current = second_num
            self.ip_val = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        elif self.op == 'sub':
            self.total -= self.current
        elif self.op == 'mul':
            self.total *= self.current
        elif self.op == 'div':
            self.total /= self.current
        elif self.op == 'mod':
            self.total %= self.current

        self.ip_val = True
        self.check_sum = False
        self.display(self.total)

    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.ip_val = True
        self.check_sum = True
        self.op = op
        self.result = False


root.mainloop()
