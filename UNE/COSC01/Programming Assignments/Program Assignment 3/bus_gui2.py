#!/usr/bin/env python3
from tkinter import *

root = Tk()
root.title("Cleanliness Rater")
root.geometry("500x100")
root.minsize(500, 100)
root.maxsize(500, 100)
root.resizable(False, False)

totalRating = 0

def rating(value):
    global totalRating
    totalRating += value
    myLabel2.config(text=f"This bus has a cleanliness rating of {totalRating:.2f}")

myLabel1 = Label(root, text="Rate the cleanliness of the bus:")
myLabel2 = Label(root, text="Please Select a Rating")

myButton1 = Button(root, text=":-(", padx=25, borderwidth=4, state=DISABLED)
myButton2 = Button(root, text="1", padx=25, borderwidth=4, command=lambda: rating(1))
myButton3 = Button(root, text="2", padx=25, borderwidth=4, command=lambda: rating(2))
myButton4 = Button(root, text="3", padx=25, borderwidth=4, command=lambda: rating(3))
myButton5 = Button(root, text="4", padx=25, borderwidth=4, command=lambda: rating(4))
myButton6 = Button(root, text="5", padx=25, borderwidth=4, command=lambda: rating(5))
myButton7 = Button(root, text=":-)", padx=25, borderwidth=4, state=DISABLED)

myLabel1.grid(row=0, column=3, columnspan=3)
myLabel2.grid(row=3, column=3, columnspan=3)

myButton1.grid(row=2, column=1)
myButton2.grid(row=2, column=2)
myButton3.grid(row=2, column=3)
myButton4.grid(row=2, column=4)
myButton5.grid(row=2, column=5)
myButton6.grid(row=2, column=6)
myButton7.grid(row=2, column=7)

root.mainloop()