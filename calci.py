from tkinter import *
class Calci:
    def __init__(self,window):
        self.expression = ""
        self.window1 = window
        window.title("Simple Calculator")
        window.geometry("270x150")
        self.equation = StringVar() 
        self.expression_field  = Entry(window, textvariable=self.equation)
        self.expression_field.grid(columnspan=4, ipadx=70)
        self.button1 = Button(window, text=' 1 ', fg='black', bg='red', command=lambda: self.press(1), height=1, width=7) 
        self.button1.grid(row=2, column=0) 
        self.button2 = Button(window, text=' 2 ', fg='black', bg='red', command=lambda: self.press(2), height=1, width=7) 
        self.button2.grid(row=2, column=1)
        self.button3 = Button(window, text=' 3 ', fg='black', bg='red', command=lambda: self.press(3), height=1, width=7) 
        self.button3.grid(row=2, column=2) 
        self.button4 = Button(window, text=' 4 ', fg='black', bg='red', command=lambda: self.press(4), height=1, width=7) 
        self.button4.grid(row=3, column=0) 
        self.button5 = Button(window, text=' 5 ', fg='black', bg='red',command=lambda: self.press(5), height=1, width=7) 
        self.button5.grid(row=3, column=1) 
        self.button6 = Button(window, text=' 6 ', fg='black', bg='red',command=lambda: self.press(6), height=1, width=7) 
        self.button6.grid(row=3, column=2) 
        self.button7 = Button(window, text=' 7 ', fg='black', bg='red', command=lambda: self.press(7), height=1, width=7) 
        self.button7.grid(row=4, column=0) 
        self.button8 = Button(window, text=' 8 ', fg='black', bg='red',command=lambda: self.press(8), height=1, width=7) 
        self.button8.grid(row=4, column=1) 
        self.button9 = Button(window, text=' 9 ', fg='black', bg='red',command=lambda: self.press(9), height=1, width=7) 
        self.button9.grid(row=4, column=2) 
        self.button0 = Button(window, text=' 0 ', fg='black', bg='red', command=lambda: self.press(0), height=1, width=7) 
        self.button0.grid(row=5, column=0) 
        self.plus = Button(window, text=' + ', fg='black', bg='red', command=lambda: self.press("+"), height=1, width=7) 
        self.plus.grid(row=2, column=3) 
        self.minus = Button(window, text=' - ', fg='black', bg='red', command=lambda: self.press("-"), height=1, width=7) 
        self.minus.grid(row=3, column=3) 
        self.multiply = Button(window, text=' * ', fg='black', bg='red', command=lambda: self.press("*"), height=1, width=7) 
        self.multiply.grid(row=4, column=3) 
        self.divide = Button(window, text=' / ', fg='black', bg='red', command=lambda: self.press("/"), height=1, width=7) 
        self.divide.grid(row=5, column=3) 
        self.equal = Button(window, text=' = ', fg='black', bg='red', command=self.equalpress, height=1, width=7) 
        self.equal.grid(row=5, column=2) 
        self.clear = Button(window, text='Clear', fg='black', bg='red', command=self.clear, height=1, width=7) 
        self.clear.grid(row=5, column='1') 
        self.Decimal= Button(window, text='.', fg='black', bg='red', command=lambda: self.press('.'), height=1, width=7) 
        self.Decimal.grid(row=6, column=0)
    def clear(self): 
        self.expression = "" 
        self.equation.set("")
    def equalpress(self): 
        try: 
            total = str(eval(self.expression)) 
            self.equation.set(total) 
            self.expression = "" 
        except: 
            self.equation.set(" error ") 
            self.expression = ""
    def press(self,num): 
        self.expression = self.expression + str(num) 
        self.equation.set(self.expression)













