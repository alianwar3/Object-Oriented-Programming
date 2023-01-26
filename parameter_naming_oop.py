# OOP is used to conceptualize the interaction between objects
class Movie:
    def __init__(self, name, year):
        self.movie_name = name # self.name is the property, name is the parameter
        self.movie_year = year # self.year is the property, year is the parameter


matrix = Movie('The Matrix', 1994)
print(matrix.movie_name) # You can access the property of matrix like this
print(matrix.movie_year)