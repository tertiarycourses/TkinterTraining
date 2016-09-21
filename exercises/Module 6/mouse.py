from tkinter import *
root = Tk()

# def mouse_press(event):
#     print("Hello")
# root.bind('<ButtonPress>', mouse_press)

def click(event):
    print("clicked at", event.x, event.y)

# frame = Frame(root, width=100, height=100)
# frame.bind("<Button-1>", click)
# frame.pack()

root.mainloop()
