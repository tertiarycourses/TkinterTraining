from tkinter import *      
    
root = Tk()

w = Text(root,  width = 40, height = 10)
w.pack()
w.config(wrap = 'word')
text= w.get('1.0', 'end')

# print(w.get('1.0', '1.end'))
# w.insert('1.0 + 2 lines', 'Inserted message')
# w.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.')
# w.delete('1.0')
# w.delete('1.0', '1.0 lineend')
# w.delete('1.0', '3.0 lineend + 1 chars')
# w.replace('1.0', '1.0 lineend', 'This is the first line.')

# w.config(state = 'disabled')
# w.delete('1.0', 'end')
# w.config(state = 'normal')

# w.tag_add('my_tag', '1.0', '1.0 wordend')
# w.tag_configure('my_tag', background = 'yellow')
# wt.tag_remove('my_tag', '1.1', '1.3')
# print(w.tag_ranges('my_tag'))
# print(tw.tag_names())
# w.replace('my_tag.first', 'my_tag.last', 'That was')
# w.tag_delete('my_tag')

# w.mark_names()
# w.insert('insert', '_')
# w.mark_set('my_mark', 'end')
# w.mark_gravity('my_mark', 'right')
# text.mark_unset('my_mark')

# image = PhotoImage(file = 'python_logo.gif').subsample(5, 5) # Change path as needed
# w.image_create('insert', image = image)
# w.image_create('insert', image = image)

# button = Button(text, text = 'Click Me')
# text.window_create('insert', window = button)

root.mainloop()
print(text)
