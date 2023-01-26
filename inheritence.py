class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)



class WorkingStudent(Student): # WorkingStudent is a class of Student, has access to parents properties and methods
    def __init__(self, name, school, salary):
        super().__init__(name, school) # super() is the parent class, will pass argument to parent class
        self.salary = salary

    @property # turns this method into something that is useful outside of WorkingStudent class, use it only when your calculating from the property objects themselves
    def weekly_salary(self):
        return self.salary * 37.5


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.name)    # name is being called in Student class, that the child class (WorkingStudent) has access to
print(rolf.school)  # school is being called in the Student class, that the child class (WorkingStudent) has access to
rolf.marks.append(57) # the child class (WorkingStudent) has access to property marks, thereby appending 57
rolf.marks.append(99) # the child class (WorkingStudent) has access to property marks, thereby appending 99
print(rolf.marks)   # Print marks
print(rolf.average()) # Calculate average

# Parent class do not have access to the child classes properties and methods, however if a child class inherits from
# a parent class, it has access to its properties and methods.

print(rolf.weekly_salary) # this will print the definition of this method