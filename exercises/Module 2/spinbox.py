from tkinter import *
from tkinter import ttk        
    
root = Tk()

year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()

root.mainloop()
print(year.get())
