from tkinter import *        
    
root = Tk()

num = IntVar()

Radiobutton(root, text = '1', variable = num,
		value = '1').pack()
Radiobutton(root, text = '2', variable = num,
		value = '2').pack()
Radiobutton(root, text = '3', variable = num,
		value = '3').pack()
Radiobutton(root, text = '1+', variable = num,
		value = '1').pack()

mainloop()
print(num.get()) 

