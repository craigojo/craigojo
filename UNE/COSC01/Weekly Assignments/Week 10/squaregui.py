
from tkinter import *
from tkinter import ttk
import turtle

def square():
    for i in range(4):
        turtle.fd(100)
        turtle.lt(90)


# square(bob)

root = Tk()
root.title('Square Drawerer')

frame = ttk.Frame(root, padding='3 3 12 12')
frame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

craigo = turtle.Turtle()
g_button = ttk.Button(frame, text='CraiGo', command=square)
g_button.grid(column=3, row=3, sticky=W)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)



root.mainloop()
