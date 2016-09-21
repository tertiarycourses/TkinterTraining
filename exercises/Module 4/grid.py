from tkinter import *   
    
root = Tk()

# Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0)
# Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1)
# Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0)
# Label(root, text = 'Yellow', background = 'Yellow').grid(row = 1, column = 1)

Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0)
Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1)
Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2)
Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, columnspan = 2)

# root.rowconfigure(0, weight = 1)
# root.rowconfigure(1, weight = 3)
# root.columnconfigure(2, weight = 1)

root.mainloop()
