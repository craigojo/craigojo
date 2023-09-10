import tkinter as tk

mywindow = tk.Tk()

def buttonPress():
    print("Button Pressed!!")

def textBox():
    print(textb.get())
    
def slideValue():
    print (Slider.get())


# Label
label = tk.Label(mywindow, text="Label Text")
label.grid(row=0,column=1)

# Button
button = tk.Button(mywindow,text='Press',command=buttonPress)
button.grid(row=1,column=1)

# Textbox
textb = tk.Entry(mywindow,text="Entry")
textbutton = tk.Button(mywindow,text="Text Box",command=textBox)
textb.grid(row=2,column=1)
textbutton.grid(row=2,column=2)

# Slider
Slider = (tk.Scale(mywindow,label=('Slider'),variable=0))
SliderButton = (tk.Button(mywindow,text='Slider',command=slideValue))
Slider.grid(row=3,column=1)
SliderButton.grid(row=3,column=2)

#Keyboard Inputs
def func_return(event):
    print ("You hit return")
mywindow.bind("<Return>", func_return)

def func_w(event):
    print ("You hit w")
mywindow.bind("<KeyPress-w>", func_w)

# Defining the window size
mywindow.geometry("300x200")
# Fixing the window size
mywindow.resizable(width=False, height=False)
# Title bar Title
mywindow.title('My Title')
# Title Bar Icon
# mywindow.iconbitmap('birdy_icon.ico')
mywindow.mainloop()