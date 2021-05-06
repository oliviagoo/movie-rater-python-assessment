#version 16 - improving the search result output
from tkinter import *
from tkinter.scrolledtext import *

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
        self.movies_list.append(Movie("Mary Poppins"))
        self.movies_list.append(Movie("The Lion King"))
        self.movies_list.append(Movie("The Wizard of Oz"))
        self.movies_list.append(Movie("E.T. the Extra Terrestrial"))

        #setting up the variables needed
        self.search_results = []
        self.position = 0
        self.rating = StringVar()
        self.rating.set(self.movies_list[self.position].rating)
        self.search_rate = []
        
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
            rb = Radiobutton(rb_frame, text = rating, value = rating, variable = self.rating, command = self.set_rate)
            rb.grid(row = RATINGS.index(rating), column = 0, sticky = W)
            self.rating_list.append(rb)

        rb_frame.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.back_but = Button(self.rate_frame, text = "Previous", command = self.go_back, state = DISABLED)
        self.back_but.grid(row = 2, column = 0)

        self.next_but = Button(self.rate_frame, text = "Next", command = self.go_next)
        self.next_but.grid(row = 2, column = 1)

        self.update_label = Label(self.rate_frame, text = "")
        self.update_label.grid(row = 3, column = 0, columnspan = 2)

        self.rate_frame.grid(row = 0, column = 0, sticky = N, pady = 10)

        #setting up the search frame
        search_frame = Frame(parent, bg = "#f5f5f5")
        
        search_label = Label(search_frame, text = "Search for movies with a rating of: ", bg = "#f5f5f5")
        search_label.grid(row = 0, column = 0, pady = 5)

        search_cb_frame = Frame(search_frame)
        self.search_buts = []
        for rating in RATINGS:
            v = StringVar()
            self.search_buts.append(Checkbutton(search_cb_frame, text = rating, onvalue = rating, offvalue = "*", variable = v, bg = "#fafafa", command = self.enable_but))
            self.search_buts[RATINGS.index(rating)].var = v
            self.search_buts[RATINGS.index(rating)].deselect()
            self.search_buts[RATINGS.index(rating)].grid(row = 0, column = RATINGS.index(rating), pady = 3)

        search_cb_frame.grid(row = 1, column = 0, pady = 5)

        self.search_but = Button(search_frame, text = "Go!", command = self.search, state = DISABLED)
        self.search_but.grid(row = 2, column = 0)

        search_frame.grid(row = 1, column = 0, sticky = S)

        #setting up the summary frame
        self.summ_frame = Frame(parent)

        self.info_label = Label(self.summ_frame, text = "")
        self.info_label.grid(row = 0, column = 0)

        self.movie_display = ScrolledText(self.summ_frame, width = 35, height = 10, wrap = "word")
        self.movie_display.grid(row = 1, column = 0, padx = 10)

        self.search_number = Label(self.summ_frame, text = "")
        self.search_number.grid(row = 2, column = 0)

        back_rate_but = Button(self.summ_frame, text = "Back to rating", command = self.back_rate)
        back_rate_but.grid(row = 3, column = 0, pady = 10)
        
    #a method that sets the rating for a movie
    def set_rate(self):
        self.movies_list[self.position].rating = self.rating.get()
        self.update_label.configure(text = "{} has been rated {}".format(self.movies_list[self.position].name, self.rating.get()))

    #a method that moves to the next movie in the list
    def go_next(self):
        self.position += 1
        self.movie_label.configure(text = self.movies_list[self.position].name)
        self.check_pos()
        self.rating.set(self.movies_list[self.position].rating)
        self.update_label.configure(text = "")

    #a method that moves to the previous movie in the list
    def go_back(self):
        self.position -= 1
        self.movie_label.configure(text = self.movies_list[self.position].name)
        self.check_pos()
        self.rating.set(self.movies_list[self.position].rating)
        self.update_label.configure(text = "")

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

    #a method that hides the rating frame and shows the summary frame
    def search(self):
        #clearing all the necessary variables and removing rating frame
        self.search_results.clear()
        self.search_rate.clear()
        self.rate_frame.grid_remove()
        self.summ_frame.grid(row=0, column = 0)

        #emptying the movie display scrolled text
        self.movie_display.configure(state = "normal")
        self.movie_display.delete("1.0", END)
        self.movie_display.configure(state = "disabled")

        #seeing which ratings are being searched for
        for option in self.search_buts:
            if option.var.get() != "*":
                self.search_rate.append(RATINGS[self.search_buts.index(option)])

        #gathering all the movies with relevant ratings
        for movie in self.movies_list:
            if movie.rating in self.search_rate:
                self.search_results.append(movie)

        #displaying the movie results
        self.movie_display.configure(state = "normal")
        if len(self.search_results) < 1:
            self.movie_display.insert(END, "There are no movies with this rating!")
        else:
            for title in self.search_results:
                if title.rating != RATINGS[0]:
                    self.movie_display.insert(END, title.name + "\n")
                    self.movie_display.insert(END, "    - {}/5".format(title.rating) + "\n", "title_rating")
                else:
                    self.movie_display.insert(END, title.name + "\n")
                    self.movie_display.insert(END, "    - {}".format(title.rating) + "\n", "title_rating")
                
                self.movie_display.tag_config("title_rating", foreground="blue")
        self.movie_display.configure(state = "disabled")

        #configuring the info label
        search_string = ", ".join(self.search_rate)
        self.info_label.configure(text = "You have given the following movies a rating of {}:".format(search_string))

        self.search_number.configure(text = "{} movies found for this search.".format(len(self.search_results)))

    #a method that hides the summary frame and shows the rating frame
    def back_rate(self):
        self.summ_frame.grid_remove()
        self.rate_frame.grid()
        self.update_label.configure(text = "")

    #if none of the checkbuttons are selected the go button will be disabled, otherwise it will be normal
    def enable_but(self):
        selected = False
        for option in self.search_buts:
            if option.var.get() != "*":
                selected = True
                break
        if selected == True:
            self.search_but.configure(state = NORMAL)
        else:
            self.search_but.configure(state = DISABLED)

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Movie Rating Program")
    MovieRater = MovieRaterGUI(root)
    root.mainloop()


