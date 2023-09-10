from tkinter import *

root = Tk()
root.title("Initialisation Error")
root.geometry("500x100")
root.minsize(150, 75)
root.maxsize(150, 75)
root.resizable(False, False)
myLabel = Label(root, text="Initialisation error." + "\n" + " Please restart the App. " + "\n" + "Contact admin for support.")

myLabel.pack()

root.mainloop()





# root = Tk()
# root.geometry("500x100")
# root.minsize(150, 75)
# root.maxsize(150, 75)
# root.resizable(False, False)
# myLabel = Label(root, text="Initialisation error." + "\n" + " Please restart the App. " + "\n" + "Contact admin for support")
# myLabel.pack()
# root.mainloop()
