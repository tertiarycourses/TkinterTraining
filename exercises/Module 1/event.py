from tkinter import *

class HelloApp:

    def __init__(self, root):

        self.label = Label(root, text = "Who are you")
        self.label.grid(row = 0, column = 0)
        
        Button(root, text = "Click Me", command = self.update).grid(row = 1, column = 0)


    def update(self):
        self.label.config(text = 'I am Alfred')

            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()


