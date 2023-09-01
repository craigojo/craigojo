from tkinter import *
from tkinter import ttk
root = Tk()
frame = ttk.Fram(root, width = 400, height = 400)
frame.grid()
image = PhotoImage(file = "tux.jpg")
label1 = ttk.Label(frame, image = image)
label2 = ttk.Label(frame, image = image)
label3 = ttk.Label(frame, image = image)
label4 = ttk.Label(frame, image = image)
label1.grid(column = 1, row = 2)
label2.grid(column = 2, row = 1)
label3.grid(column = 2, row = 3)
label4.grid(column = 3, row = 2)

           