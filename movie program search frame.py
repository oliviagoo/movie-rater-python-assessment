#version 5 - setting up the search frame

from tkinter import *

RATINGS = ["No Rating", "1", "2", "3", "4", "5"]

class MovieRaterGUI:
    def __init__(self, parent):
        self.search_rate = StringVar()

        search_frame = Frame(parent)

        search_label = Label(search_frame, text = "Search for movies with a rating of: ")
        search_label.grid(row = 0, column = 0)

        search_rb_frame = Frame(search_frame)
        for rating in RATINGS:
            rb = Radiobutton(search_rb_frame, text = rating, value = rating, variable = self.search_rate)
            rb.grid(row = 0, column = RATINGS.index(rating))

        search_rb_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.search_but = Button(search_frame, text = "Go!", command = self.printsearch)
        self.search_but.grid(row = 2, column = 0)

        search_frame.grid(row = 0, column = 0)

    def printsearch(self):
        print(self.search_rate.get())

#main routine
if __name__ == "__main__":
    root = Tk()
    MovieRater = MovieRaterGUI(root)
    root.mainloop()
            
