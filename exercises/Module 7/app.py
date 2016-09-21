from tkinter import *


class HelloApp:

    def __init__(self, master):

        self.label = Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)

    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')

            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()
