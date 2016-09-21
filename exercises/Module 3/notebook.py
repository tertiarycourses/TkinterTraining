from tkinter import *
from tkinter import ttk        
    
root = Tk()

w = ttk.Notebook(root)
w.pack()

frame1 = ttk.Frame(w)
frame2 = ttk.Frame(w)
w.add(frame1, text = 'One')
w.add(frame2, text = 'Two')
ttk.Button(frame1, text = 'Click Me').pack()

frame3 = ttk.Frame(w)
w.insert(1, frame3, text = 'Three')
# notebook.forget(1)
# notebook.add(frame3, text = 'Three')

w.select(2)
print(w.index(w.select()))
# w.select(2)

w.tab(1, state = 'disabled')
# w.tab(1, state = 'hidden')
# w.tab(1, state = 'normal')
# w.tab(1, 'text')
# w.tab(1)

root.mainloop()
