from tkinter import *        
from tkinter import ttk

root = Tk()

# w = PanedWindow(orient=VERTICAL)
# w.pack(fill=BOTH, expand=1)

# top = Label(w, text="top pane")
# w.add(top)

# bottom = Label(w, text="bottom pane")
# w.add(bottom)


w = ttk.PanedWindow(orient = HORIZONTAL)
w.pack(fill = BOTH, expand = True)

f1 = ttk.Frame(w, width = 100, height = 300, relief = SUNKEN)
f2 = ttk.Frame(w, width = 400, height = 400, relief = SUNKEN)
w.add(f1, weight = 1)
w.add(f2, weight = 4)

f3 = ttk.Frame(w, width = 50, height = 50, relief = SUNKEN)
w.insert(1, f3)

top = Label(f1, text="top pane")
top.pack()

# bottom = Label(w, text="bottom pane")
# w.add(bottom)

# panedwindow.forget(1)

root.mainloop()
