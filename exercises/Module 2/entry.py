from tkinter import *       
    
root = Tk()

v = StringVar()
w = Entry(root, width = 30, textvariable=v).pack()

# w.delete(0, 1)
# w.delete(0, END)

# w.insert(0, 'Enter your password')
# w.config(show = '*')
#w.state(['disabled'])
# w.state(['readonly'])
# w.state(['!disabled'])

root.mainloop()
print(v.get())
