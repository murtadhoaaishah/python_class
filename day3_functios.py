# def function():
#     print("Hello World")
# function()

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(*kids): # * indicates the number of parameter is not yet
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

#Keyword argument: You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitarary keyword arguments: ** is used when number of argoments is not unknown
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


#Default parameter Value
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


#Passing a List as an Argument
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# import math
# def interest(principal= int, rate=int <= 100, time = int):
#   # time_in_year = math.floor(time/12)
#   print(int(principal * rate * (math.floor(time/12) ) / 100))
# interest(24, 10, 10)




# def count_movies_by_genre():
#     movie_list = []
    
#     movie_input = int(input("Enter the number of movies: "))
    
#     for _ in range(movie_input):
#         title = input("Enter movie title: ")
#         genre = input("Enter movie genre: ")
#         movie_list.append({'title': title, 'genre': genre})
    
#     print("Movie list:", movie_list)
    
#     genre_counts = {}
#     for movie in movie_list:
#         genre = movie.get('genre')
#         if genre:
#             if genre in genre_counts:
#                 genre_counts[genre] += 1
#             else:
#                 genre_counts[genre] = 1
    
#     return genre_counts

# genre_counts = count_movies_by_genre()
# print("Genre counts:", genre_counts)


movies = [
    ["Casablanca", "Michael Curtiz", 1942, "Drama"],
    ["The Godfather", "Francis Ford Coppola", 1972, "Crime"],
    ["The Shawshank Redemption", "Frank Darabont", 1994, "Drama"],
    ["The Dark Knight", "Christopher Nolan", 2008, "Action, Thriller"],
    ["Living in Bondage", "Ola Balogun", 1992, "Drama"],
    ["Nneka the Pretty Serpent", "Christian Chukwu", 1994, "Drama, Thriller"],
    ["Rattlesnake", "Amaka Igwe", 1995, "Crime, Thriller"],
    ["Aki na Ukwa", "Chico Ejiro", 2002, "Comedy"],
    ["Saworo IDE", "unknown ", 1997, "Drama"]
]

def movie_counter():
  genre_list = []
  for movie in movies:
    movie_genre = movie[2].split(",")    
  #   genre_list.append(movie_genre)
  #   if genre_list.count()
    print(movie_genre)
movie_counter()