from tkinter import *
from tkinter import ttk

def insert_line(text, user, line):
  """ A function to allow adding lines to the conversation easier"""
  text.insert("end", str(user) + ": " + str(line) + "\n")

# Set up window
root = Tk()
root.title("Chatter")

# Set up required variables
usernames = ["alice", "bob", "charlie", "dianne", "ethan", "freda", "gary", "helen"]
variable = StringVar()
choices = StringVar(value = usernames)  # you'd really get this to be a list of logged-in users

# Set up widgets
content = ttk.Frame(root)
output = Text(content)
chat_scroll = ttk.Scrollbar(content, orient = VERTICAL, command = output.yview)
output["yscrollcommand"] = chat_scroll.set
label = ttk.Label(content, text = "bob:")  # you'd really set this when the user logs in
entry = ttk.Entry(content, textvariable = variable)
button = ttk.Button(content, text = "Send")
users = Listbox(content, listvariable = choices)
user_scroll = ttk.Scrollbar(content, orient = VERTICAL, command = users.yview)
users["yscrollcommand"] = user_scroll.set

# Place widgets
output.grid(row = 1, column = 1, columnspan = 2, sticky = (N, S, W, E))
chat_scroll.grid(row = 1, column = 3, sticky = (N, S, W))
label.grid(row = 2, column = 1, sticky = E)
entry.grid(row = 2, column = 2, sticky = (E, W))
button.grid(row = 2, column = 3, columnspan = 2, sticky = W, pady = 10)
users.grid(row = 1, column = 4, sticky = (N, S, W, E), padx = (5, 0))
user_scroll.grid(row = 1, column = 5, sticky = (N, S, W))
content.grid(sticky = (N, S, W, E))

# Configure resizing
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

content.columnconfigure(1, weight = 1)
content.columnconfigure(2, weight = 3)
content.columnconfigure(3, weight = 1)
content.columnconfigure(4, weight = 3)
content.columnconfigure(5, weight = 1)

content.rowconfigure(1, weight = 1)

# add conversation
insert_line(output, "gary", "did you see the latest:")
insert_line(output, "gary", "http://www.dailydot.com/politics/encryption-crypto-wars-backdoors-timeline-security-privacy/")
insert_line(output, "helen", "Not yet - what's it about")
insert_line(output, "gary", "the crypto war")
insert_line(output, "bob", "I saw that yesterday")
insert_line(output, "helen", "I'll go look at it now")
insert_line(output, "bob", "It's become more of a political issue than it really should be")
insert_line(output, "bob", "I mean it's all well known now, there's no way to really stop it")
insert_line(output, "helen", "Interesting")
insert_line(output, "helen", "Yes, making encryption illegal would mean only outlaws had encryption")
insert_line(output, "bob", "Exactly!")
insert_line(output, "gary", "hopefully they'll realise that")
insert_line(output, "alice", "Hi everybody!")
insert_line(output, "helen", "Hi alice!")
insert_line(output, "bob", "Hey")
insert_line(output, "alice", "What's happening?")
insert_line(output, "helen", "Nothing much")
insert_line(output, "charlie", "I just got here too")
insert_line(output, "bob", "We've been discussing the latest war on encryption")
insert_line(output, "alice", "I really don't understand it")
insert_line(output, "alice", "I mean, without strong encryption, nobody has privacy")
insert_line(output, "gary", "I certainly wouldn't trust Internet banking without it")
insert_line(output, "charlie", "you couldnt!")

variable.set("It'd basically be making maths illegal")

# stop output from being editable
output["state"] = "disabled"

# start main loop
root.mainloop()