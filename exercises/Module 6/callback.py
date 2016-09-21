from tkinter import *

def callback():
	print(1)

# def callback(x):
# 	print(x)

root = Tk()

Button(root, text = 'Click Me 1', command = callback()).pack()

# Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
# Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
# Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()


# Button(root, text = 'Click Me 1', command = lambda: print(1)).pack()
# Button(root, text = 'Click Me 2', command = lambda: print(2)).pack()
# Button(root, text = 'Click Me 3', command = lambda: print(3)).pack()


root.mainloop()


