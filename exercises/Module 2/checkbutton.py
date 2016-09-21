from tkinter import *

root = Tk()

s = StringVar()
s.set('Name')

w = Checkbutton(root, text = 'Who?')
w.pack()

w.config(variable = s, onvalue = 'Alfred', offvalue = 'Ally')
mainloop()

print(s.get())

