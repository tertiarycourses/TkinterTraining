from tkinter import *
from tkinter import ttk 

root = Tk()
#w = Button(root, text="Click Me!")
w = ttk.Button(root, text="Click Me!")
w.pack()

# w['text'] = "Push Me"
# w.config(text="Push Me")

# def callback():
#     print('Clicked!')
# w.config(command = callback)

# w.state(['disabled'])
# w.instate(['disabled'])

# w.state(['!disabled'])
# w.instate(['!disabled'])

# logo = PhotoImage(file = 'python_logo.gif') 
# w.config(image = logo, compound = LEFT)
# small_logo = logo.subsample(5, 5)
# w.config(image = small_logo)


root.mainloop()