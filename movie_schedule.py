currentMovies={"The Grinch": "11:00am",
               "Rudolph": "1:00pm",
               "Frosty the Snowman": "3:00pm",
                "Christmas Vacation": "5:00pm"}

print("We are showing the following movies")

for key in currentMovies:
    print(key)
movie=input("What movie would you like the showtime for?\n")

showtime=currentMovies.get(movie)

if showtime==None:
    print("The requested movie is not playing")

else:
    print(movie, "is playing at", showtime)
