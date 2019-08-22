from tkinter import *

expression = ""

#Basic Setup 
window = Tk()
window.title("Calculator App")
window.geometry("250x150")
t = StringVar()
textfield = Entry(window, textvariable = t)
t.set("Enter your values")
textfield.grid(columnspan=4) 

#OPERATIONS
def press(num):
    global expression
    expression += str(num)
    t.set(expression)
    
def equal():
    global expression
    total = str(eval(expression))
    t.set(total)

def clear():
    global expression
    expression = ""
    t.set(expression)

#LAYOUT
#Number Button
btn1 = Button(window, text= '1', command=lambda: press(1), height=1, width=7) 
btn1.grid(row=2, column=0) 

btn2 = Button(window, text='2', command=lambda: press(2), height=1, width=7) 
btn2.grid(row=2, column=1) 

btn3 = Button(window, text='3', command=lambda: press(3), height=1, width=7) 
btn3.grid(row=2, column=2) 

btn4 = Button(window, text='4', command=lambda: press(4), height=1, width=7) 
btn4.grid(row=3, column=0) 

btn5 = Button(window, text='5', command=lambda: press(5), height=1, width=7) 
btn5.grid(row=3, column=1) 

btn6 = Button(window, text='6', command=lambda: press(6), height=1, width=7) 
btn6.grid(row=3, column=2) 

btn7 = Button(window, text='7', command=lambda: press(7), height=1, width=7) 
btn7.grid(row=4, column=0) 

btn8 = Button(window, text='8', command=lambda: press(8), height=1, width=7) 
btn8.grid(row=4, column=1) 

btn9 = Button(window, text='9', command=lambda: press(9), height=1, width=7) 
btn9.grid(row=4, column=2) 

btn0 = Button(window, text='0', command=lambda: press(0), height=1, width=7) 
btn0.grid(row=5, column=0) 



# Operations
plus = Button(window, text='+', command=lambda: press("+"), height=1, width=7) 
plus.grid(row=2, column=3) 

minus = Button(window, text='-', command=lambda: press("-"), height=1, width=7) 
minus.grid(row=3, column=3) 

multiply = Button(window, text='*', command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 

divide = Button(window, text='/', command=lambda: press("/"), height=1, width=7) 
divide.grid(row=5, column=3) 

equal = Button(window, text='=', command=equal, height=1, width=7) 
equal.grid(row=5, column=2) 

clear = Button(window, text='Clear', command=clear, height=1, width=7) 
clear.grid(row=5, column='1') 


window.mainloop()