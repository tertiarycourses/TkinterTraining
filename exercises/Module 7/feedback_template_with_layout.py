from tkinter import *

class Feedback:

    def __init__(self, master):    

        self.frame_header = Frame(master)
        self.frame_header.pack()
        
        self.logo = PhotoImage(file = 'tour_logo.gif')
        Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        Label(self.frame_header, text = 'Thanks for Exploring!').grid(row = 0, column = 1)
        Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

        self.frame_content = Frame(master)
        self.frame_content.pack()
        
        Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = Entry(self.frame_content, width = 24)
        self.entry_email = Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        Button(self.frame_content, text = 'Submit').grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        Button(self.frame_content, text = 'Clear').grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
