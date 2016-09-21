from tkinter import *
from tkinter import ttk        
    
root = Tk()

# f1 = ttk.Frame(root)
# f1.pack()
# f1.config(height = 100, width = 200)
# f1.config(relief = RIDGE)
# f2 = ttk.Frame(root)
# f2.pack()
# f2.config(height = 300, width = 400)
# f2.config(relief = SUNKEN)

# Button(f1, text = 'Click Me on Frame 1').pack()
# Button(f2, text = 'Click Me on Frame 2').pack()
#f1.config(padding = (300, 150))
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

root.mainloop()
