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