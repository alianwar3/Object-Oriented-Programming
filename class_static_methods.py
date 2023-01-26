class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student('Rolf', 'MIT')

rolf.marks.append(57) # the child class (WorkingStudent) has access to property marks, thereby appending 57
rolf.marks.append(99) # the child class (WorkingStudent) has access to property marks, thereby appending 99

print(rolf.average()) # instance method


# Use @classmethod whenever you want to use something that doesn't need 'self'
# Use @staticmethod when class is not going to get inheritted from parent
class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

new_number = FixedFloat.from_sum(19.575, 0.789) # We can use from_sum directly from the FixedFloat class
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'Euro {self.symbol}{self.amount:.2f}'

money = Euro.from_sum(16.758, 9.999)
print(money)