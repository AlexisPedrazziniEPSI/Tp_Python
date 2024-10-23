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
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def area(self):
        return self.largeur * self.hauteur

class ShapeFactory:
    @staticmethod
    def create(shape_type, **kwargs):
        if shape_type == "circle":
            return Circle(kwargs['radius'])
        elif shape_type == "rectangle":
            print("We do red rectangle now ?")
            return Rectangle(kwargs['largeur'], kwargs['hauteur'])
        else:
            raise ValueError("Connais pas ton truc géométrique, reviens avec des cercles ou des rectangles")

# Example test
shape1 = ShapeFactory.create(shape_type="circle", radius=5)
assert isinstance(shape1, Circle)
assert round(shape1.area(), 2) == 78.54

shape2 = ShapeFactory.create(shape_type="rectangle", largeur=3, hauteur=4)
assert isinstance(shape2, Rectangle)
assert shape2.area() == 12