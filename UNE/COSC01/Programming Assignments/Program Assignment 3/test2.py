#!/usr/bin/env python3
from tkinter import *

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

        my_label1.grid(row=0, column=3, columnspan=3)
        my_label2.grid(row=3, column=3, columnspan=3)

        my_button1.grid(row=2, column=1)
        my_button2.grid(row=2, column=2)
        my_button3.grid(row=2, column=3)
        my_button4.grid(row=2, column=4)
        my_button5.grid(row=2, column=5)
        my_button6.grid(row=2, column=6)
        my_button7.grid(row=2, column=7)
    except Exception as widget_error:
        print(f"Widget Creation error: {widget_error} Please restart the App, and contact the Administrator for support if the issue persists")

def rating(value, label):
    global total_rating
    try:
        if 1 <= value <= 5:
            total_rating += value
            label.config(text=f"This bus has a cleanliness rating of {total_rating:.2f}")
        else:
            raise ValueError("Rating should be between 1 and 5.")
    except ValueError as invalid_entry:
        label.config(text=str(invalid_entry))

root = Tk()
root.title("Cleanliness Rater")
root.geometry("500x100")
root.minsize(500, 100)
root.maxsize(500, 100)
root.resizable(False, False)

total_rating = 0

create_widget()

root.mainloop()
