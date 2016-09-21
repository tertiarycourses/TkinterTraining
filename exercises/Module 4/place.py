from tkinter import *   
    
root = Tk()
root.geometry('640x480+200+200')

Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 5)
Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5,anchor='center')
Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely=0.5,y=50)
Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5,anchor='ne')

# Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
# Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
# Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
# Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

root.mainloop()
