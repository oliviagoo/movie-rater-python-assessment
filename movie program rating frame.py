#version 4 - adding the back button functionality
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
        self.movies_list.append(Movie("The Titanic"))
        self.movies_list.append(Movie("Jurassic Park"))
        self.movies_list.append(Movie("Spirited Away"))
        self.position = 0
        self.rating = StringVar()
        self.rating.set(self.movies_list[self.position].rating)

        self.rate_frame = Frame(parent)
        self.rate_frame.grid(row = 0, column = 0)

        instruction_label = Label(self.rate_frame, text = "Please rate:")
        instruction_label.grid(row = 0, column = 0)

        self.movie_label = Label(self.rate_frame, text = self.movies_list[self.position].name)
        self.movie_label.grid(row = 0, column = 1)

        rating_label = Label(self.rate_frame, text = "Your rating:")
        rating_label.grid(row = 1, column = 0, sticky = N, pady = 10)

        rb_frame = Frame(self.rate_frame)
        self.rating_list = []
        for rating in RATINGS:
            rb = Radiobutton(rb_frame, text = rating, value = rating, variable = self.rating, command = self.printrate)
            rb.grid(row = RATINGS.index(rating), column = 0, sticky = W)
            self.rating_list.append(rb)

        rb_frame.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.back_but = Button(self.rate_frame, text = "Previous", command = self.go_back, state = DISABLED)
        self.back_but.grid(row = 2, column = 0)

        self.next_but = Button(self.rate_frame, text = "Next", command = self.go_next)
        self.next_but.grid(row = 2, column = 1)
        
        self.rate_frame.grid(row = 0, column = 0)

    def printrate(self):
        print(self.rating.get())
        self.movies_list[self.position].rating = self.rating.get()
        print(self.movies_list[self.position].rating)

    def go_next(self):
        self.position += 1
        self.movie_label.configure(text = self.movies_list[self.position].name)
        self.check_pos()
        self.rating.set(self.movies_list[self.position].rating)

    def go_back(self):
        self.position -= 1
        self.movie_label.configure(text = self.movies_list[self.position].name)
        self.check_pos()
        self.rating.set(self.movies_list[self.position].rating)
        
    def check_pos(self):
        if self.position == len(self.movies_list) - 1:
            self.next_but.configure(state = DISABLED)
        else:
            self.next_but.configure(state = NORMAL)
            
        if self.position == 0:
            self.back_but.configure(state = DISABLED)
        else:
            self.back_but.configure(state = NORMAL)

#main routine
if __name__ == "__main__":
    root = Tk()
    MovieRater = MovieRaterGUI(root)
    root.mainloop()
