from tkinter import *


class Feedback:

    def __init__(self, master):    

        self.frame_header = Frame(master)
        
        self.logo = PhotoImage(file = '../images/tour_logo.gif')
        Label(self.frame_header, image = self.logo)
        Label(self.frame_header, text = 'Thanks for Exploring!')
        Label(self.frame_header, text = ("We're glad you chose Explore Californiafor your recent adventure.  "
                                             "Please tell us what you thought about the 'Desert to Sea' tour."))

        self.frame_content = Frame(master)
        self.frame_content.pack()
        
        Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = Entry(self.frame_content, width = 24)
        self.entry_email = Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        Button(self.frame_content, text = 'Submit')
        Button(self.frame_content, text = 'Clear')

def main():            
    
    root = Tk()
    app = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()