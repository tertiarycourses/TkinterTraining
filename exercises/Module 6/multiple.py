from tkinter import *
           
root = Tk()

label = Label(root, text = 'Label 1')
label.pack()

label.bind('<ButtonPress>', lambda e: print('Button Press'))
label.bind('<2>', lambda e: print('Mouse Press'))

root.mainloop()
