from tkinter import *

root = Tk()
root.geometry('100x100')
root.title("Amazing Button")

def greetings():
    print("Hello World")

Label(root, text = "Hi there").pack(side=TOP)

Button(root, text = "Greetings", command = greetings).pack(side = LEFT)
Button(root, text = "Exit", command = root.destroy).pack(side = RIGHT)

mainloop()