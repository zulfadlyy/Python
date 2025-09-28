# super() = Function used to give access to methods of a parent class.
#           Returns a temporary object of a parent class when used.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width) # Call the __init__ method of the parent class

    def area(self):
        return self.length * self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width) # Call the __init__ method of the parent class
        self.height = height # New attribute

    def volume(self):
        return self.length * self.width * self.height

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())