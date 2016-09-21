from tkinter import *
from tkinter import ttk 

root = Tk()
#w = Label(root, text="Hello, Tkinter!")
w = ttk.Label(root, text="Hello, Tkinter!")
w.pack()

# w.config(wraplength = 150)
# w.config(foreground = 'blue')
# w.config(background = 'yellow')
# w.config(font = ('Courier',18,'bold'))

# logo = PhotoImage(file = 'python_logo.gif') 
# w.config(image = logo)
# w.config(compound = 'text')
# w.config(compound = 'center')
# w.config(compound = 'left')

root.mainloop()
