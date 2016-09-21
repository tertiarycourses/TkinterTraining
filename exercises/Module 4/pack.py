from tkinter import *      
    
root = Tk()

Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10)


root.mainloop()
