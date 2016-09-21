from tkinter import *

def key_press(event):
    print(event.char)
   
root = Tk()

root.bind('<KeyPress>',key_press)

root.mainloop()
