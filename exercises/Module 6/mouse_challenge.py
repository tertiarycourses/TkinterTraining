from tkinter import *

def mouse_press(event):
    global prev
    prev = event

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event

root = Tk()

canvas = Canvas(root, width = 640, height = 480, 
                background = 'white')
canvas.pack()
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()
