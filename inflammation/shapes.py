import math


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


mycircle = Circle(15)
myrect = Rectangle(10, 5)
myshapes = [mycircle, myrect]
print(sum(myshape.get_area() for myshape in myshapes))
