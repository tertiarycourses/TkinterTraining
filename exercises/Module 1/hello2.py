from tkinter import *

def printHello():
	print("Hello")

root = Tk()

Button(root,text='Click Me', command = printHello).pack()

root.mainloop()
