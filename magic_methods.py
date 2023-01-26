class Student:
    def __init__(self, name):
        self.name = name


movies = ['Matrix', 'Finding Nemo']
print(movies.__class__) # A list is an object in python


class Garage:
    def __init__(self):
        self.cars = []


    # Return length of the list
    def __len__(self):
        return len(self.cars)


    # Return element in a list
    def __getitem__(self, i):
        return self.cars[i]


    # Returns everything we need to read the object, useful for when your debugging
    def __repr__(self):
        return f'Garage with {self.cars} cars.'


    # Useful for printing things out to users
    def __str__(self):
        return f'Garage with {len(self.cars)} cars.'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
# print(ford[0]) # Garage.__getitem__(ford, 0)

# When you have __getitem__ in your class, you can use a for loop to
# go through each of the elements in the list
for car in ford:
    print(car)

print(ford) # Being printed from __str__



# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []


    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]
    def __getitem__(self, i):
        return f'{self.players[i]}'


    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name}: {list_of_players}
    # the club_name and list_of_players should be replaced by the according value of current object
    def __repr__(self):
        return f'Club {self.name}: {self.players}'


    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name} with {count_of_players} players
    # the club_name and count_of_players should be replaced by the according value of current object
    def __str__(self):
        return f'Club {self.name} with {len(self.players)}'

# You only need to finish the methods, we will take care of the object creation and call those methods for you!

#1 - Set club name
some_club = Club('Arsenal')

#2 - Append players to list
some_club.players.append('Rolf')
some_club.players.append('Anne')

#3 - Access i -th player in my_club
print(some_club[0]) # Runs through __getitem___

#4 - Return string representation of players in club
print(some_club) # Runs through __str__