from tkinter import *

root = Tk()

c = Canvas(root)
c.pack()
c.config(width = 640, height = 480)

#line = c.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
# c.itemconfigure(line, fill = 'green')
# print(c.coords(line))
# c.coords(line, 0, 0, 320, 240, 640, 0)

# c.itemconfigure(line, smooth = True)
# c.itemconfigure(line, splinesteps = 5)
# c.itemconfigure(line, splinesteps = 100)
# c.delete(line)

# rect = c.create_rectangle(160, 120, 480, 360)
# c.itemconfigure(rect, fill = 'yellow')
#oval = c.create_oval(160, 120, 480, 360)
# arc = c.create_arc(160, 1, 480, 240)
# c.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
#poly = c.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')
text = c.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

# logo = PhotoImage(file = 'python_logo.gif') # Change path as needed
# image = c.create_image(320, 240, image = logo)

# c.lift(text)
# c.lower(image)
# c.lower(image, text)

button = Button(c, text = 'Click Me')
c.create_window(320, 60, window = button)

# canvas.itemconfigure(rect, tags = ('shape'))
# canvas.itemconfigure(oval, tags = ('shape', 'round'))
# canvas.itemconfigure('shape', fill = 'grey')
# print(canvas.gettags(oval))

root.mainloop()
