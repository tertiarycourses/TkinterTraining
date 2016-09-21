from tkinter import *
from tkinter import ttk        
    
root = Tk()

w = ttk.Treeview(root)
w.pack()
w.insert('', '0', 'item1', text = 'First Item')
w.insert('', '1', 'item2', text = 'Second Item')
w.insert('', 'end', 'item3', text = 'Third Item')

# logo = PhotoImage(file = 'C:\\Users\\barron\\Dropbox\\Lynda Courses\\Python GUI Development with Tkinter\\Exercise Files - Current\\03 Widget Classes\\python_logo.gif').subsample(10,10)
# w.insert('item2', 'end', 'python', text = 'Python', image = logo)

# w.config(height = 5)
w.move('item2', 'item1', 'end')
w.item('item1', open = True)
# w.item('item2', open = True)
#print(w.item('item1', 'open'))

#w.detach('item3')
#w.move('item3', 'item2', '0')
w.delete('item3')

# treeview.configure(column = ('version'))
# treeview.column('version', width = 50, anchor = 'center')
# treeview.column('version', width = 50, anchor = 'center')
# treeview.column('#0', width = 150)
# treeview.heading('version', text = 'Version')
# treeview.set('python', 'version', '3.4')
# treeview.item('python', tags = ('software'))
# treeview.tag_configure('software', background = 'yellow')

# def callback(event):
#     print(treeview.selection())

# treeview.bind('<<TreeviewSelect>>', callback)

# treeview.config(selectmode = 'browse')
# print(treeview.selection_add('python'))
# print(treeview.selection_remove('python'))
# print(treeview.selection_toggle('python'))

root.mainloop()
