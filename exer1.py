from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def area(self):
        return self.largeur * self.hauteur

circle = Circle(5)
assert round(circle.area(), 2) == 78.54

rectangle = Rectangle(3, 4)
assert rectangle.area() == 12