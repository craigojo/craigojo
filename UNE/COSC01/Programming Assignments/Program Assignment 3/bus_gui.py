#!/usr/bin/env python3


# Functions required for the program are imported (tkinker)
import tkinter as tk


# Variable are created
total_rating = 0            # Stores total value for all ratings (input values of each click from user interface)
ratings = 0
title = "Cleanliness Rater"
space = ' '
extra_space = space * 97        # Ratings counter. The variable stores total number of ratings (number of user input clicks from user interface)





# import required module
from tkinter import *
 
 
# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
 
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", lambda toggle_colour: button.config(
        background=colorOnHover))
 
    # background color on leving widget
    button.bind("<Leave>", lambda toggle_colour: button.config(
        background=colorOnLeave))


# Function created. Responds to inputs from the user interface (fixed input values from user button clicks)
def rating(value):


    # Sets Global access for required variables outside the try block.
    global total_rating, ratings


    # Try block contains error checking. Implemented for highly unlikely scenarios where two buttons are simultaneously clicked.
    try:
        if value >= 1 and value <= 5:
            ratings += 1                                                                # Increments the ratings counter by 1
            total_rating += value                                                       # Adds value of rating to total_rating variable
            rating_average = total_rating / ratings                                     # Calculates the rating average, the resulatant output is returned to 
                                                                                        # the user interface, value displayed has two decimal places
            rating_selected.config(
                text=f"This bus has an average cleanliness rating of {rating_average:.2f}")
            

        # Exception errors are handled here            
        else:
            raise ValueError("Rating should be between 1 and 5.")
    except ValueError as invalid_entry:
        rating_selected.config(text=str(invalid_entry))


# Creates the user interface
root = tk.Tk()
root.title(f".{extra_space}{title}")                # Displayed in the title bar 
root.geometry("750x95")
root.eval('tk::PlaceWindow . center')                         # Sets the overall window size
root.minsize(750, 95)                           # Window size minimum value, fixed value
root.maxsize(750, 95)                           # Window size maximum value, fixed value
root.resizable(False, False)                    # Restricts window size from changes, fixed value


# Sets row 1 an row 3 text, font size and centered.
my_label1 = tk.Label(root, anchor="center",font="10", text="Rate the cleanliness of the bus:")
rating_selected = tk.Label(root, anchor="center",font="10", text="Please select a rating, 1 = Poor... 5 = Excellent")


# Creates buttons, button text and button fixed values.
my_button1 = tk.Button(root, text=":-(", padx=10, borderwidth=4, state=tk.DISABLED)
my_button2 = tk.Button(root, text="1", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(1))
my_button3 = tk.Button(root, text="2", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(2))
my_button4 = tk.Button(root, text="3", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(3))
my_button5 = tk.Button(root, text="4", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(4))
my_button6 = tk.Button(root, text="5", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(5))
my_button7 = tk.Button(root, text=":-)", padx=10, borderwidth=4, state=tk.DISABLED)


# call function with background
# colors as argument

changeOnHover(my_button2, "aliceblue", "lightgrey")
changeOnHover(my_button3, "aliceblue", "lightgrey")
changeOnHover(my_button4, "aliceblue", "lightgrey")
changeOnHover(my_button5, "aliceblue", "lightgrey")
changeOnHover(my_button6, "aliceblue", "lightgrey")

# Sets label positions
my_label1.grid(row=0, column=2, columnspan=6)
rating_selected.grid(row=3, column=2, columnspan=6)


# Sets button positions, and spacing around buttons
my_button1.grid(row=2, column=1, padx=(33, 0), pady=(5, 5))
my_button2.grid(row=2, column=2, padx=(0, 0), pady=(5, 5))
my_button3.grid(row=2, column=3, padx=(0, 0), pady=(5, 5))
my_button4.grid(row=2, column=4, padx=(0, 0), pady=(5, 5))
my_button5.grid(row=2, column=5, padx=(0, 0), pady=(5, 5))
my_button6.grid(row=2, column=6, padx=(0, 0), pady=(5, 5))
my_button7.grid(row=2, column=7, padx=(0, 10), pady=(5, 5))


# Continues the Tkinter application, loops to root.
root.mainloop()


 







