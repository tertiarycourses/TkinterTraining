from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()

# w = Label(root, text="Hello, world!")
# w.pack()
# root.mainloop()

w = Scale(root,from_= 0,to = 100, orient = HORIZONTAL)
w.pack()
root.mainloop()

#root.geometry('800x600')
# c = Canvas(root,width=800, height=600)
# c.pack()

# r = c.create_rectangle(0,0,50,50,fill='red', outline='red')
