from tkinter import *
from tkinter import ttk        
    
root = Tk()

w = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
w.pack()

w.config(mode = 'indeterminate')
w.start()
w.stop()

# w.config(mode = 'determinate', maximum = 11.0, value = 4.2)
# w.config(value = 8.0)
w.step()
w.step(5)

# value = DoubleVar()
# w.config(variable = value)

# scale = ttk.Scale(root, orient = HORIZONTAL,
# 		  length = 400, variable = value,
# 		  from_ = 0.0, to = 11.0)
# scale.pack()
# scale.set(4.2)
# print(scale.get())

root.mainloop()
