from tkinter import *
from tkinter import ttk        
    
root = Tk()

value = DoubleVar()

def update(value):
	print(value)

# w = ttk.Scale(root, orient = HORIZONTAL,
# 		  length = 400, variable = value,
# 		  from_ = 0.0, to = 11.0)
w = ttk.Scale(root, orient = HORIZONTAL,
		  length = 400, variable = value,
		  from_ = 0.0, to = 11.0,command=update)
w.pack()
#w.set(4.2)

root.mainloop()
print(value.get())