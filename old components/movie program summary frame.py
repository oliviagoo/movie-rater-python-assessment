#version 7 - setting up the summary frame GUI
from tkinter import *
from tkinter.scrolledtext import *

RATINGS = ["No Rating", "1", "2", "3", "4", "5"]

class MovieRaterGUI:
    def __init__(self, parent):
        self.search_rate = StringVar()
        
        self.summ_frame = Frame(parent)

        info_label = Label(self.summ_frame, text = "You have given the following movies a rating of {}:".format(self.search_rate.get()))
        info_label.grid(row = 0, column = 0)

        self.movie_display = ScrolledText(self.summ_frame, width = 50, height = 10, wrap = "word")
        self.movie_display.grid(row = 1, column = 0, padx = 10)

        self.movie_display.insert(END, "Example text \nExample text etc. etc. etc. \n\n\n\n\nexample\n\nmore example text\n\n\n")
        self.movie_display.configure(state = "disabled")

        back_rate_but = Button(self.summ_frame, text = "Back to rating")
        back_rate_but.grid(row = 2, column = 0)

        self.summ_frame.grid(row = 0, column = 0)

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Movie Rating Program")
    MovieRater = MovieRaterGUI(root)
    root.mainloop()
