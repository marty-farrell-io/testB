class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

def calculate_perimeter(radius):
    return 2 * 3.14 * radius

# Creating an object of the Circle class
circle = Circle(5)

# Calling the method to calculate the area
area = circle.calculate_area()

# Calling the function to calculate the perimeter
perimeter = calculate_perimeter(5)

print("Area:", area)
print("Perimeter:", perimeter)

print(2 + 2 * 6 + 4 - 8 * 18 +1)