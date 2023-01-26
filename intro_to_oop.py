# We can think of functions as:
#   -> Stores data
#   -> Actions to work with that data


# Flaw is in the software design
#   -> average function is not related to my_student
my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],
    'average': None # we cannot put a method here that will act with the data inside of my_student
}

average = lambda grades: sum(grades) / len(grades)
total_avg = average(my_student['grades'])



# Class defines what the object is stored
class Student:

    # Step 2 -> Immediately calls the __init__ function
    #   -> This gets passed to self (an empty object)
    def __init__(self, new_name, new_grades):

        # Step 3 -> Inside the empty object, we are defining the name and grades variable
        self.name = new_name # Creating a property of the object called name
        self.grades = new_grades # Creating a property of the object called grades


    # A function in a class is called a method
    def average(self, add):
        return sum(self.grades) / len(self.grades) + add


student_one = Student('Rolf Smith', [70, 88, 90, 99]) # Step 1 -> Creates a new object of Student
student_two = Student('Jose', [50, 60, 99, 100])
# print(student_one.__class__) # Prints the type

print(student_one.average(2))
print(student_two.average(5))
# print(Student.average(student_one, 2)) # student_one is being passed as 'self'


# Example of Movie class
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    # let's try to add a method `print_info()` here:
    def print_info(self):
        return f"<<{self.name}>> by {self.director}"


# You only need to finish the method, we will take care of the object creation and call your method for you!
my_movie = Movie('The Matrix', 'Wachowski')
output = my_movie.print_info()
print(output)