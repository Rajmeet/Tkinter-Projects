from tkinter import *

window = Tk()
t = StringVar()

window.title('Simple app')
window.geometry('350x350')

Label(window, text="Name").grid(column = 0, row = 0)
Entry(window, width = 20, textvariable = t).grid(column=1,row = 0)

def clicked():
    a = t.get()
    print(a)


Button(window, text = "Click Me", command = clicked).grid(column = 0, row = 1)
Button(window, text= 'Exit', command = window.destroy).grid(column = 1 , row = 1)

mainloop()