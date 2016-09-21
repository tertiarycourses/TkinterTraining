from tkinter import *

def update():
	label.config(text = 'Paris')
          
           
root = Tk()
label = Label(root, text = 'Answer')
label.pack()
        
Button(root, text = "Capital of France", command = update).pack()
root.mainloop()
    


