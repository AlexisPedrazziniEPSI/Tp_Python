import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        return NotImplemented

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

norm_v1 = v1.norm()
assert round(norm_v1, 2) == 3.74

dot_product = v1 * v2
assert dot_product == 32  # Produit scalaire

v3 = v1 + v2
assert v3.x == 5 and v3.y == 7 and v3.z == 9