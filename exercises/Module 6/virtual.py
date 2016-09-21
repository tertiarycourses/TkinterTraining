from tkinter import *
        
root = Tk()

entry = Entry(root)
entry.pack()

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

root.mainloop()
