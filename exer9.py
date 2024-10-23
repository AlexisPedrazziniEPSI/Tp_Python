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