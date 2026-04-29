# Base class (Abstraction)
class Shape:
    def area(self):
        pass   # abstract method

    def draw(self):
        pass   # abstract method


# Subclass 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        return "Drawing Circle"


# Subclass 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def draw(self):
        return "Drawing Rectangle"


# Subclass 3
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        return "Drawing Triangle"


# Main function (testing polymorphism)
def main():
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 8)
    ]

    for shape in shapes:
        print(shape.draw())
        print("Area:", shape.area())
        print("-----")


main()