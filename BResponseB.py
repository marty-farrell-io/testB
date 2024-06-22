class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person1 = Person("John", 30)
person1.greet()  # This is a method call

def calculate_age(birth_year):
    current_year = 2022
    return current_year - birth_year

age = calculate_age(1990)  # This is a function call
print(age)