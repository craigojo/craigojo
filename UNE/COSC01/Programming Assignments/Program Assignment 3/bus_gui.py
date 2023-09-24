#!/usr/bin/env python3


'''
Bus Cleanliness App.
Records cleanliness for the school bus. Passengers select a rating 1 to 5. 
The app provides an average rating for all selections.
'''

# Functions required for the program are imported (tkinker)
import tkinter as tk
from tkinter import *
import platform



# Variables created here.
# Stores total value for all ratings (input values of each click from user interface).
total_rating = 0

# Ratings counter. Stores total number of ratings (number of input clicks from user interface).       
ratings = 0



'''
Functions are defined here.
'''

def gui_window_setup(root):
# Exception handling applied for unlikely scenarios where system platform info is not determined.
    try:
        system_info = platform.system()
        if system_info: pass
    except Exception as system_error:
        print(f"An error occurred: {system_error}")

    if platform.system() == "Windows":                      # Sets title position Windows OS
        title = "Cleanliness Rater"
        space = ' '
        padding = space * 73
        # Title bar, includes release number.
        root.title(f"Release 1.0{padding}{title}")

    else:
        title = "Cleanliness Rater"                         # Sets title position Linux/Unix
        root.title(f"{title}")
    return root



# Function: Window size setup.
def gui_window_size(root):
    # Sets the GUI window size.
    window_width = int(750)
    window_height = int(105)
    screen_width = int(root.winfo_screenwidth())            # Gets system screen width
    screen_height = int(root.winfo_screenheight())          # Gets system screen height

    # Calculates centre for x and y coordinates on system screen.
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
                                                            # Centres GUI to system screen.
    root.geometry(
        f"{window_width}x{window_height}+{x}+{y}"
        )                                  
    root.minsize(750, 105)                                  # Window size minimum, fixed value.
    root.maxsize(750, 105)                                  # Window size maximum, fixed value.
    root.resizable(False, False)                            # Restricts window size from changes, fixed value.
    return root

 

# Function: Adjusts properties of buttons on hover.
def change_on_hover(button, colorOnHover, colorOnLeave):
 
    # Implements button background colour on entering.
    button.bind("<Enter>", lambda toggle_colour: button.config(
        background=colorOnHover))
 
    # Implements button background colour on leaving.
    button.bind("<Leave>", lambda toggle_colour: button.config(
        background=colorOnLeave))



# Function: Responds to inputs from user interface (fixed input values from user button clicks).
def rating(value):

    global total_rating, ratings                            # Sets Global access for variable counters.

    # Try block contains error checking. 
    # Implemented for highly unlikely scenarios where two or more buttons are simultaneously clicked.
    try:
        if value >= 1 and value <= 5:
            ratings += 1                                    # Increments the ratings counter by 1.
            total_rating += value                           # Adds value of rating to total_rating variable.

            # Calculates the rating average, the resulatant output is returned to
            # the user interface, value is displayed to two decimal places.
            rating_average = total_rating / ratings
            rating_selected.config(
                text=f"This bus has an average cleanliness rating of {rating_average:.2f}")
            

        # Exception errors are handled here.           
        else:
            raise ValueError("Rating should be between 1 and 5.")
    except ValueError as invalid_entry:
        rating_selected.config(text=str(invalid_entry))



'''
Application is started, GUI created.
'''

# Start.
root = tk.Tk()

gui_window_setup(root)                                      # Calls function, gui_window_title
gui_window_size(root)                                       # Calls function, gui_window_size


# Sets row 1 an row 3 text, font size and centres.
my_label1 = tk.Label(root, anchor="center", font=('Arial', 10), text="Rate the cleanliness of the bus:")
rating_selected = tk.Label(root, anchor="center", font=('Arial', 10), text="Please select a rating, 1 = Poor... 5 = Excellent")


# Calls function, rating . Creates buttons, text, colour, size, button fixed values.
my_button1 = tk.Button(root, text=":-(", padx=10, borderwidth=4, state=tk.DISABLED)
my_button2 = tk.Button(root, text="1", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(1))
my_button3 = tk.Button(root, text="2", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(2))
my_button4 = tk.Button(root, text="3", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(3))
my_button5 = tk.Button(root, text="4", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(4))
my_button6 = tk.Button(root, text="5", bg="lightgrey", padx=50, borderwidth=4, command=lambda: rating(5))
my_button7 = tk.Button(root, text=":-)", padx=10, borderwidth=4, state=tk.DISABLED)


# Calls function, change_on_hover. Sets buttons hover colour.
# Colours as argument for each button.
change_on_hover(my_button2, "aliceblue", "lightgrey")
change_on_hover(my_button3, "aliceblue", "lightgrey")
change_on_hover(my_button4, "aliceblue", "lightgrey")
change_on_hover(my_button5, "aliceblue", "lightgrey")
change_on_hover(my_button6, "aliceblue", "lightgrey")

# Sets label positions.
my_label1.grid(row=0, column=2, columnspan=6, padx=(0, 60), pady=(5,0))
rating_selected.grid(row=3, column=2, columnspan=6, padx=(0, 60), pady=(5,0))


# Sets button positions, and spacing around buttons.
my_button1.grid(row=2, column=1, padx=(33, 0), pady=(5, 5))
my_button2.grid(row=2, column=2, padx=(0, 0), pady=(5, 5))
my_button3.grid(row=2, column=3, padx=(0, 0), pady=(5, 5))
my_button4.grid(row=2, column=4, padx=(0, 0), pady=(5, 5))
my_button5.grid(row=2, column=5, padx=(0, 0), pady=(5, 5))
my_button6.grid(row=2, column=6, padx=(0, 0), pady=(5, 5))
my_button7.grid(row=2, column=7, padx=(0, 10), pady=(5, 5))


# Continues the Tkinter application, loops to root.
root.mainloop()


 







