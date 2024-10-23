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

class BankAccount:
    def __init__(self, balance):
        assert balance > 0, "Le compte doit avoir de l'argent"
        self.balance = balance

    def __add__(self, montant):
        self.balance += montant
        return self

    def __sub__(self, montant):
        self.balance -= montant
        return self

    def __str__(self):
        return f"Le solde du compte est de {self.balance} euros"

account = BankAccount(100)
account += 20
assert account.balance == 120

account -= 50
assert account.balance == 70

def check_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("x doit être positif")
        return func(x)
    return wrapper

@check_positive
def double(x):
    return x * 2

assert double(5) == 10
try:
    double(-1)
except ValueError:
    print("Exception levée correctement")

class Car:
    def __init__(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value <= 0:
            raise ValueError("La vitesse doit être positive")
        if value > 200:
            raise ValueError("La vitesse doit être inférieure ou égale à 200")
        self._speed = value

# Exemple de test
car = Car()
car.speed = 120
assert car.speed == 120

try:
    car.speed = 250  # Doit lever une exception
except ValueError:
    print("Vitesse non valide")

class InvalidAgeError(Exception):
    pass

class Person:
    def __init__(self, prenom,age):
        if age > 150:
            raise InvalidAgeError("L'âge doit être inférieur à 150")
        elif age < 0:
            raise InvalidAgeError("L'âge doit être positif")

try:
    person = Person("John", 200)
except InvalidAgeError:
    print("Age non valide")

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = {}
            self.initialized = True

    def create_context(self): #
        return DatabaseContext(self)

class DatabaseContext:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.operations = []

    def add_entry(self, entry_id, data):
        self.db_connection.data[entry_id] = data

    def delete_entry(self, entry_id):
        if entry_id in self.db_connection.data:
            del self.db_connection.data[entry_id]

    def drop_all(self):
        self.db_connection.data.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


db = DatabaseConnection()

with db.create_context() as based:
    based.add_entry(1, "data1")
    based.add_entry(2, "data2")
    based.delete_entry(1)

assert db.data == {2: 'data2'}

with db.create_context() as based:
    based.drop_all()

assert db.data == {}

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

import threading
import time
from functools import wraps


class TimeoutError(Exception):
    """Exception levée lorsque la limite de temps est dépassée."""
    pass


def timeout_limit(timeout, raise_exception=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Variable pour stocker l'exception
            result = [None]
            exc = [None]

            # Fonction interne exécutée dans un thread séparé
            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exc[0] = e

            # Démarrage du thread pour exécuter la fonction
            thread = threading.Thread(target=target)
            thread.start()

            # Attente pendant la durée spécifiée
            thread.join(timeout)

            # Si le thread est toujours actif après le timeout
            if thread.is_alive():
                if raise_exception:
                    raise TimeoutError("Exécution interrompue par raise_exception.")
                else:
                    raise TimeoutError("La limite de temps a été dépassée.")

            # Si une exception a été levée dans le thread, la relancer
            if exc[0]:
                raise exc[0]

            return result[0]

        return wrapper

    return decorator


# Exemple d'utilisation :
@timeout_limit(5, raise_exception=False)
def long_task():
    print("Tâche longue démarrée")
    time.sleep(10)  # Simuler une tâche longue
    print("Tâche longue terminée")


try:
    long_task()
except TimeoutError as e:
    print(e)

class Matrix:
    def __init__(self, data):
        # Vérification que chaque ligne a la même longueur
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Toutes les lignes doivent avoir la même longueur.")
        self.values = data  # Changer data à values

    def __add__(self, other):
        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            raise ValueError("Les matrices doivent avoir les mêmes dimensions pour l'addition.")

        # Addition des matrices
        result = [
            [
                self.values[i][j] + other.values[i][j]
                for j in range(len(self.values[0]))
            ]
            for i in range(len(self.values))
        ]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.values[0]) != len(other.values):
            raise ValueError("Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième.")

        # Multiplication des matrices
        result = [
            [
                sum(self.values[i][k] * other.values[k][j] for k in range(len(other.values)))
                for j in range(len(other.values[0]))
            ]
            for i in range(len(self.values))
        ]
        return Matrix(result)

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def create(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError("Autre chose qu'une créature d'australie stp")
dog = AnimalFactory.create(animal_type="dog", name="Buddy")
assert isinstance(dog, Dog)
assert dog.speak() == "Woof"

cat = AnimalFactory.create(animal_type="cat", name="Misty")
assert isinstance(cat, Cat)
assert cat.speak() == "Meow"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price

product1 = Product("Apple", 1.50)
product2 = Product("Banana", 1.20)

assert product1 > product2

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Le dépôt ne peut pas être inférieur à 0.")
        self._balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Le dépôt ne peut pas être inférieur à 0.")
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            raise ValueError("Solde insuffisant.")
        self._balance -= amount

account = Account()
account.balance = 100

try:
    account.withdraw(150)  # Doit lever une exception
except ValueError:
    print("Solde insuffisant")

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
assert v3.x == 4 and v3.y == 6

v4 = v1 * 2
assert v4.x == 2 and v4.y == 4