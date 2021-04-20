#version 1 - setting up the tkinter and the support class
from tkinter import *

RATINGS = ["No Rating", "1", "2", "3", "4", "5"]

class Movie:
    def __init__(self, name, rating = RATINGS[0]):
        self.name = name
        self.rating = rating

class MovieRaterGUI:
    def __init__(self, parent):
        self.movies_list = []
        self.movies_list.append(Movie("The Hobbit"))
        self.position = 0
        self.rating = self.movies_list[self.position].rating

        self.rate_frame = Frame(parent)
        self.rate_frame.grid(row = 0, column = 0)

        instruction_label = Label(self.rate_frame, text = "Please rate:")
        instruction_label.grid(row = 0, column = 0)

        self.movie_label = Label(self.rate_frame, text = self.movies_list[self.position].name)
        self.movie_label.grid(row = 0, column = 1)

        rating_label = Label(self.rate_frame, text = "Your rating:")
        rating_label.grid(row = 1, column = 0)

        rb_frame = Frame(self.rate_frame)
        self.rating_list = []
        for rating in RATINGS:
            rb = Radiobutton(rb_frame, text = rating, value = rating, variable = self.rating, command = self.printrate)
            rb.grid(row = RATINGS.index(rating), column = 0)

        rb_frame.grid(row = 1, column = 1)
        self.rate_frame.grid(row = 0, column = 0)

    def printrate(self):
        print(self.rating)

#main routine
if __name__ == "__main__":
    root = Tk()
    MovieRater = MovieRaterGUI(root)
    root.mainloop()
