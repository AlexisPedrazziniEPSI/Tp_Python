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