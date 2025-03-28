class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"({self.x}I, {self.y}J, {self.z}K)"
    
    
v1 = Vector(1, 2, 3)
v2 = Vector(2, 3, 4)
v3 = Vector(3, 4, 5)

print(v1 + v2)
print(v3 + v1)
print(v1 * v3)