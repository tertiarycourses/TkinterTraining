from tkinter import *
from tkinter import ttk 

root = Tk()

# Module 7 : Demo



# Module 6 Events Handling

# Multiple Events
# w = Label(root, text="Label 1")
# w.pack()

# w.bind('<ButtonPress>', lambda e:print('Button Press'))
# w.bind('<2>',lambda e: print("Press 2"))
# root.mainloop()

# Virtual Event

# def printOdd(event):
# 	print('Odd Number!')

# entry = Entry(root)
# entry.pack()
# entry.event_add('<<OddNumber>>','1','3','5','7','9')
# entry.bind('<<OddNumber>>',printOdd)
# root.mainloop()

# Binding to Mouse

# def mouse_press(event):
# 	print("x:{}, y:{}".format(event.x,event.y))

# root.bind('<ButtonPress>',mouse_press)

# Binding to Keyboard
# def keyprint(event):
# 	print('event.char')
# def printCopy(event):
# 	print('Copy')
# def printPaste(event):
# 	print('Paste')

#root.bind('<KeyPress>',keyprint)
# root.bind('<Control-C>',printCopy)
# root.bind('<Control-V>',printPaste)


# Callback Commands
# a = lambda x: x*x
# print(a(5))

# def callback(num):
# 	print(num)

# Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
# Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
# Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()
# root.mainloop()

# Module 5: Shapes


# c = Canvas(root)
# c.pack()
# c.config(width=600,height=600)
# b = Button(c, text = 'Click Me')
# c.create_window(320, 60, window = b)

# poly = c.create_polygon(160,360,320,480,480,360,fill='blue')
# text = c.create_text(200,200,text='polygon',font=('Courier',32,'bold'))
# arc = c.create_arc(50,50,200,200)
# c.itemconfigure(arc, start=0, extent= 180, fill='red',width=5)

# oval = c.create_oval(150,150,50,100)
# c.itemconfigure(oval,fill='red')
# rect = c.create_rectangle(50,50,150,150)
# c.itemconfigure(rect,fill='blue')

# line= c.create_line(10,10,50,50,fill='blue',width=5)
# c.itemconfigure(line,fill='green')
# c.coords(line,50,50,100,0)
# Module 4: Geometry Management

# Place

# f1 = ttk.Frame(root, width=200,height=400,relief=RIDGE).grid(row=0,column=0,columnspan=2)
# f2 = ttk.Frame(root, width=400,height=200,relief=RIDGE).grid(row=0,column=1)
# f3 = ttk.Frame(root, width=400,height=200,relief=RIDGE).grid(row=1,column=2)
# Label(f1, text = 'Nav').pack()
# Label(f2, text = 'Text').pack()
# Label(f3, text = 'Control').pack()



# Label(f, text = 'Hello',background = 'green').place(relx=0.5,rely=0.25)
# Label(f, text = 'Hello',background = 'orange').place(relx=0.25,rely=0.5,anchor='center')
# Label(f, text = 'Hello',background = 'yellow').place(relx=0.75,rely=0.5)
# Label(f, text = 'Hello',background = 'blue').place(relx=0.5,rely=0.75,anchor='ne')


# Grid
# Label(root, text = 'Hello',background = 'green').grid(row=1,column=1)
# Label(root, text = 'Hello',background = 'orange').grid(row=1,column=0)
# Label(root, text = 'Hello',background = 'yellow').grid(row=0,column=0,columnspan=2)
# Label(root, text = 'Hello',background = 'blue').grid(row=2,column=0,columnspan=2)

# Label(root, text = 'Hello',background = 'green').grid(row=0,column=0)
# Label(root, text = 'Hello',background = 'orange').grid(row=0,column=1)
# Label(root, text = 'Hello',background = 'yellow').grid(row=0,column=2,rowspan=2)
# Label(root, text = 'Hello',background = 'blue').grid(row=1,column=0,columnspan=2)

# Pack
# w = Frame(root,width=100,height=100).pack()

# Label(w, text = 'Hello',
#   background = 'yellow').pack(side=LEFT,padx=10,pady=10)
# Label(w, text = 'Hello',
#   background = 'blue').pack(side=LEFT,ipadx=10,ipady=10)
# Label(w, text = 'Hello',
#           background = 'green').pack(side=LEFT)



# Module 3: Organizing Widgets

# Notebook

# w = ttk.Notebook(root)
# w.pack()
# f1 = ttk.Frame(w,width=50,height=50)
# f2 = ttk.Frame(w,width=100,height=200)
# w.add(f1,text='One')
# #Text(f1,width=200,height=200).pack()
# Label(f1,text="Hello").pack()
# w.add(f2,text='Two')
# Text(f2,width=100,height=100).pack()

# Paned Window

# w = ttk.PanedWindow(orient = HORIZONTAL)
# w.pack(fill = BOTH, expand = True)

# f1 = ttk.Frame(w, width = 100, height = 300, relief = SUNKEN)
# f2 = ttk.Frame(w, width = 200, height = 400, relief = SUNKEN)
# w.add(f1,weight=1)
# w.add(f2,weight=2)

# f3 = ttk.Frame(w, width = 300, height = 50, relief = SUNKEN)
# Label(f3,text="Frame3").pack()
# w.insert(2, f3)
#w.add(f3,weight=3)

# top = Label(f1, text="top pane")
# top.pack()

# Windows

# w1 = Toplevel(root)
# w1.title('Window 1')
# w1.geometry('200x100+50+50')
# w1.resizable(True,True)
# w1.maxsize(300,300)

# w2 = Toplevel(root)
# w2.title('Window 2')
# w2.geometry('300x300+100+100')
# w2.destroy()


# w1.lift(w2)
# w2.lift(root)
# w1.lower(w2)


# Frames
# f1 = ttk.Frame(root)
# f1.pack()
# f1.config(height=100,width=200)
# f1.config(relief=RIDGE)

# Label(f1, text="Hello on Frame 1").pack(side=LEFT)
# Button(f1, text = 'Click Me on Frame 1').pack(side=RIGHT)


# f2 = ttk.Frame(root)
# f2.pack()
# f2.config(height=300,width=400)
# f2.config(relief=SUNKEN)

# Label(f2, text="Hello on Frame 2").pack(side=LEFT)
# Button(f2, text = 'Click Me on Frame 2').pack(side=RIGHT)




# Syling

# style = ttk.Style()
# style.theme_use('default')

# def callback():
# 	label.config(text='Paris!')

# label = Label(root, text="What is the Capital of France!")
# label.pack()
# button = Button(root)
# button.pack()
# button.config(text='Show Answer',command=callback)

#Scrollbar

# sx = ttk.Scrollbar(root, orient = HORIZONTAL)
# sy = ttk.Scrollbar(root, orient = VERTICAL)
# sx.pack(side=BOTTOM,fill=X)
# sy.pack(side=RIGHT,fill=Y)

# text = Text(root, width=40, height=20, xscrollcommand=sx.set, yscrollcommand=sy.set)
# for i in range(1000):
#     text.insert(END, str(i))
# text.pack(side=LEFT, fill=BOTH)
# text.config(wrap="none")
# sy.config(command=text.yview)
# sx.config(command=text.xview)

# Menu
#root.option_add('*tearOff', False)
# menubar = Menu(root)
# root.config(menu = menubar)
# file = Menu(menubar)
# edit = Menu(menubar)
# help_ = Menu(menubar)

# Module 2 Widgets

# Treeview (List)
# w = ttk.Treeview(root)
# w.pack()
# w.insert('', '0', 'item1', text = 'First Item')
# w.insert('', '1', 'item2', text = 'Second Item')
# w.insert('', 'end', 'item3', text = 'Third Item')
# w.insert('', 'end', 'item4', text = 'Fourth Item')
# w.move('item2','item1','end')
# w.move('item3','item1','0')
# w.move('item4','item3','end')
# w.item('item1',open=True)
# w.item('item3',open=True)
#w.detach('item4')
#w.delete('item4')

# Scale Bar
# w = Scale(root,from_= 0,to = 100, orient = HORIZONTAL)
# w.pack()

# Progress Bar
# w = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
# w.pack()
# w.config(mode = 'indeterminate')
# w.start()
# w.stop()

#w.config(mode = 'determinate', maximum = 11.0, value = 2)
# w.config(value = 8.0)
# w.step()
# w.step()
# w.step()
# w.step()
# w.step(5)


# Spin Box
# year = StringVar()
# Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()

# root.mainloop()
# print(year.get())

#Combo Box
# month = StringVar()
# combobox = ttk.Combobox(root,textvariable=month)
# combobox.pack()
# combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# month.set('Dec')
# root.mainloop()
# print(month.get())
# Text

# s = StringVar()
# w = Text(root,width=20,height=5)
# w.pack()
# w.config(wrap='word')
# w.insert('2.0','1111\n2222\n3333')
# w.delete('2.0','2.end')
# # s = w.get('1.0','1.end')
# root.mainloop()
# print(s)

#Entry
# s = StringVar()
# w = Entry(root,width=30,textvariable=s)
# w.pack()
# w.insert(0,'Enter your password')
# w.config(show="*")
# w.delete(0,END)
# w.config(state='disabled')
# w.config(state='normal')
# root.mainloop()
# print(s.get())

# Radio Button
# MODES = [ ("Monochrome", "M"), ("Grayscale", "G"), ("True color", "RGB"), ("Color separation", "CMYK")]
# v = StringVar()
# def showMode():
# 	print(v.get())
# for text, mode in MODES:
# 	Radiobutton(root, text=text, variable=v, value=mode, command=showMode).pack(anchor='w')
# a = IntVar()
# def showInt():
# 	print(a.get())
# Radiobutton(root,text='1',value='1',variable=a,command=showInt).pack()
# Radiobutton(root,text='2',value='2',variable=a,command=showInt).pack()
#Radiobutton(root,text='3',value='1').pack()
# root.mainloop()
#print(a.get())

# Check Button
# s = StringVar()
# s.set('No')
# w = ttk.Checkbutton(root,text='Hungry?')
# w.pack()
# w.config(variable=s,onvalue="Yes",offvalue="No")

# root.mainloop()
# print(s.get())

# a = IntVar()
# a.set(5)
# print(a.get())
# Button
# def callback():
# 	label.config(text='Paris!')

# label = Label(root, text="What is the Capital of France!")
# label.pack()
# button = Button(root)
# button.pack()
# button.config(text='Show Answer',command=callback)

# def callback():
# 	print('Thanks!')

# w = Button(root)
# w.pack()
# w.config(text='Click Me',command=callback)
# w.config(state='disabled')
# w.config(state='active')
# logo = PhotoImage(file='../images/python_logo.gif')
# small_logo = logo.subsample(10,10)
# w.config(image=small_logo,compound=LEFT)

#w['text']='Click Me'

# Label
#w = Label(root, text="Hello!",foregroun='blue',background='yellow')
# w = Label(root, text="Hello!")
# w.pack()
# logo = PhotoImage(file='../images/python_logo.gif')
# w.config(image=logo)
# w.config(foreground='blue')
# w.config(background='yellow')
# w.config(font=('Courier',18,'bold'))
# w.config(wraplength = 200)

# def doSomething():
# 	print("Hello!")

#Label(root, text="Hello!").pack()
#Button(root, text="Click Me", command=doSomething).pack()


#root.mainloop()