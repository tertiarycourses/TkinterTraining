from tkinter import *
from tkinter import ttk        
    
root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scrollbar.set)
for i in range(1000):
    text.insert(END, str(i))
text.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=text.yview)


# w = Text(root,  width = 400, height = 100)
# w.pack()
# #canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')
# xscroll = ttk.Scrollbar(root, orient = HORIZONTAL)
# yscroll = ttk.Scrollbar(root, orient = VERTICAL)
# w.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

# canvas.grid(row = 1, column = 0)
# xscroll.grid(row = 2, column = 0, sticky = 'ew')
# yscroll.grid(row = 1, column = 1, sticky = 'ns')

# def canvas_click(event):
#     x = canvas.canvasx(event.x)
#     y = canvas.canvasy(event.y)
#     canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

# canvas.bind('<1>', canvas_click)

root.mainloop()
