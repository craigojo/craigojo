import math
from tkinter import *
from tkinter import ttk
def calculate(*args):
    try:
        value = float(fahrenheit.get())
        celsius.set((value - 32) * (5 / 9))
    except ValueError:
        pass



root = Tk()
root.title('Fahrenheit to Celsius')
frame = ttk.Frame(root, padding='3 3 12 12')
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
fahrenheit = StringVar()
celsius = StringVar()
f_entry=ttk.Entry(frame, width=7, textvariable=fahrenheit)
f_entry.grid(column=2, row=1, sticky=(W, E))

c_label = ttk.Label(frame, textvariable=celsius)
c_label.grid(column=2, row=2, sticky=(W, E))
g_button = ttk.Button(frame, text='Go', command=calculate)
g_button.grid(column=3, row=3, sticky=W)
f_label = ttk.Label(frame, text='degrees F')
f_label.grid(column=3, row=1, sticky=W)
e_label = ttk.Label(frame, text='is equivalent to')
e_label.grid(column=1, row=2, sticky=E)
d_label = ttk.Label(frame, text='degrees C')
d_label.grid(column=3, row=2, sticky=W)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
for i in range(1, 4):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)
f_entry.focus()

root.bind('<Return>', calculate)
root.mainloop()