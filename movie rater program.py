#version 6 - combining the search and rating frames into one program
from tkinter import *

#constant list - the different ratings there are
RATINGS = ["No Rating", "1", "2", "3", "4", "5"]

#support class - each movie is an object
class Movie:
    def __init__(self, name, rating = RATINGS[0]):
        self.name = name
        self.rating = rating

#class that sets up the GUI
class MovieRaterGUI:
    def __init__(self, parent):
        #setting up the list of movies
        self.movies_list = []
        self.movies_list.append(Movie("The Hobbit"))
        self.movies_list.append(Movie("The Titanic"))
        self.movies_list.append(Movie("Jurassic Park"))
        self.movies_list.append(Movie("Spirited Away"))

        #setting up the variables needed
        self.position = 0
        self.rating = StringVar()
        self.rating.set(self.movies_list[self.position].rating)
        self.search_rate = StringVar()
        
        #setting up the rating frame
        self.rate_frame = Frame(parent)

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
            rb.grid(row = RATINGS.index(rating), column = 0, sticky = W)
            self.rating_list.append(rb)

        rb_frame.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.back_but = Button(self.rate_frame, text = "Previous", command = self.go_back, state = DISABLED)
        self.back_but.grid(row = 2, column = 0)

        self.next_but = Button(self.rate_frame, text = "Next", command = self.go_next)
        self.next_but.grid(row = 2, column = 1)

        self.rate_frame.grid(row = 0, column = 0, sticky = N, pady = 10)

        #setting up the search frame
        search_frame = Frame(parent, bg = "#f5f5f5")
        
        search_label = Label(search_frame, text = "Search for movies with a rating of: ", bg = "#f5f5f5")
        search_label.grid(row = 0, column = 0, pady = 5)

        search_rb_frame = Frame(search_frame)
        for rating in RATINGS:
            rb = Radiobutton(search_rb_frame, text = rating, value = rating, variable = self.search_rate, bg = "#fafafa")
            rb.grid(row = 0, column = RATINGS.index(rating), pady = 3)

        search_rb_frame.grid(row = 1, column = 0, pady = 5)

        self.search_but = Button(search_frame, text = "Go!", command = self.printsearch)
        self.search_but.grid(row = 2, column = 0)

        search_frame.grid(row = 1, column = 0, sticky = S)
        
    #a method that prints the rating for a movie
    def printrate(self):
        print(self.rating.get())
        self.movies_list[self.position].rating = self.rating.get()
        print(self.movies_list[self.position].rating)

    #a method that moves to the next movie in the list
    def go_next(self):
        self.position += 1
        self.movie_label.configure(text = self.movies_list[self.position].name)
        self.check_pos()
        self.rating.set(self.movies_list[self.position].rating)

    #a method that moves to the previous movie in the list
    def go_back(self):
        self.position -= 1
        self.movie_label.configure(text = self.movies_list[self.position].name)
        self.check_pos()
        self.rating.set(self.movies_list[self.position].rating)

    #a method that checks the position in the list of the current movie
    def check_pos(self):
        if self.position == len(self.movies_list) - 1:
            self.next_but.configure(state = DISABLED)
        else:
            self.next_but.configure(state = NORMAL)
            
        if self.position == 0:
            self.back_but.configure(state = DISABLED)
        else:
            self.back_but.configure(state = NORMAL)

    #a method that prints what rating should be searched for 
    def printsearch(self):
        print(self.search_rate.get())

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Movie Rating Program")
    MovieRater = MovieRaterGUI(root)
    root.mainloop()

