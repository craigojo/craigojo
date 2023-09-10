#!/usr/bin/env python3
from tkinter import *

root = None
try:
    root = Tk()
    root.title("Cleanliness Rater")
    root.geometry("500x100")
    root.minsize(500, 100)
    root.maxsize(500, 100)
    root.resizable(False, False)
    total_rating = 0
    ratings = 0
    my_label2 = Label(root, text="")
    create_widget(label_2)



except TclError:
    if root:
        root.destroy()
    root = Tk()
    root.title("Initialisation Error")
    root.geometry("150x100")
    root.minsize(150, 100)
    root.maxsize(150, 100)

    root.resizable(False, False)
    my_label = Label(root, text="Initialisation error." + "\n" + " Please restart the App. " + "\n" + "Contact admin for support.")
    my_label.grid(row=0, column=2, columnspan=2)
    my_button1 = Button(root, text="Ok", padx=25, borderwidth=4, command=root.destroy)
    my_button1.grid(row=3, column=2, columnspan=2)

def create_widget():
    try:
        my_label1 = Label(root, text="Rate the cleanliness of the bus:")
        my_label2 = Label(root, text="Please Select a Rating")

        my_button1 = Button(root, text=":-(", padx=25, borderwidth=4, state=DISABLED)
        my_button2 = Button(root, text="1", padx=25, borderwidth=4, command=lambda: rating(1, my_label2))
        my_button3 = Button(root, text="2", padx=25, borderwidth=4, command=lambda: rating(2, my_label2))
        my_button4 = Button(root, text="3", padx=25, borderwidth=4, command=lambda: rating(3, my_label2))
        my_button5 = Button(root, text="4", padx=25, borderwidth=4, command=lambda: rating(4, my_label2))
        my_button6 = Button(root, text="5", padx=25, borderwidth=4, command=lambda: rating(5, my_label2))
        my_button7 = Button(root, text=":-)", padx=25, borderwidth=4, state=DISABLED)

        my_label1.grid(row=0, colun=3, columnspan=3)
        my_label2.grid(row=3, column=3, columnspan=4)

        my_button1.grid(row=2, column=1)
        my_button2.grid(row=2, column=2)
        my_button3.grid(row=2, column=3)
        my_button4.grid(row=2, column=4)
        my_button5.grid(row=2, column=5)
        my_button6.grid(row=2, column=6)
        my_button7.grid(row=2, column=7)

    except Exception as widget_excep_error:
        label2.config(text=f"Widget Creation error: {widget_excep_error}. Please restart the App, and call the Administrator for support if the issue persists")

def rating(value, return_label):
    global total_rating, ratings
    try:
        if value >= 1 and value <= 5:
            ratings += 1
            total_rating += value
            rating_average = total_rating / ratings
            return_label.config(text=f"This bus has an average cleanliness rating of {rating_average:.2f}")
        else:
            raise ValueError("Rating should be between 1 and 5.")
    except ValueError as invalid_entry:
        return_label.config(text=str(invalid_entry))

root.mainloop()
