from tkinter import *
from tkinter import ttk

def on_scroll(*args):
    text.yview(*args)

root = Tk()
root.title('Chatter')

frame = ttk.Frame(root, padding='3 3 12 12')
frame.grid(column=0, row=0, sticky=(N, W, E, S))

text = Text(frame, width=50, height=10)
text.grid(column=0, row=0, sticky=(W, E))

# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=on_scroll)
scrollbar.grid(column=1, row=0, sticky=(N, S))

# Connect the Text widget to the scrollbar
text.config(yscrollcommand=scrollbar.set)
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")
text.insert("1.0", "gary: did you see the latest")




root.mainloop()
