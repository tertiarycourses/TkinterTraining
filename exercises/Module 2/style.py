from tkinter import *
from tkinter import ttk        
    
root = Tk()

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')      
button1.pack()
button2.pack()

style = ttk.Style()

# print(style.theme_names())
# print(style.theme_use())
#style.theme_use('default')
style.theme_use('classic')
#style.theme_use('vista')

# print(button1.winfo_class())
style.configure('TButton', foreground = 'blue')
style.configure('TButton', background = 'yellow')
# style.configure('Alarm.TButton', foreground = 'orange',
#                 font = ('Arial', 24, 'bold'))
# button2.configure(style = 'Alarm.TButton')
# style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
#                                          ('disabled', 'grey')])
# button2.state(['disabled'])

# print(style.layout('TButton'))
# print(style.element_options('Button.label'))
# print(style.lookup('TButton', 'foreground'))

root.mainloop()
