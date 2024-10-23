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