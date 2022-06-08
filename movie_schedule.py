current_movies = { "Fight Club":"11:00 am",
                   "Boondock Saints":"1:00 pm",
                   "Pulp Fiction":"3:00 pm",
                   "Bambi":"5:00 pm" 
}

print("We're showing the following movies:\n")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, "is playing at", showtime)    


