from random import randint

class Vector:
    def __init__(self, x, y, z):
        assert all(isinstance(_, (int, float)) for _ in (x, y, z))
        self.x = x
        self.y = y
        self.z = z


    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("No")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("No")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("No")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other
        else:
            raise TypeError("No")

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def vecpr(self,other):
        if isinstance(other, Vector):
            return Vector(self.y * other.z - self.z * other.y,self.x * other.z- self.z * other.x,self.x * other.y-self.y * other.x)
        else:
            raise TypeError("No")


# Координата центра масс
def centermass(vectors):
    if not vectors:
        raise TypeError("No")

    sum_x = sum(v.x for v in vectors)
    sum_y = sum(v.y for v in vectors)
    sum_z = sum(v.z for v in vectors)

    n = len(vectors)
    return Vector(sum_x / n, sum_y / n, sum_z / n)


#Треугольник с максимальной площадью
def area(v1, v2, v3):

    a = v2 - v1
    b = v3 - v1
    return abs(a.vecpr(b)) / 2


def maxarea(vectors):

    max_area = 0
    n = len(vectors)
    points=[]

    for i in range(n):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n-1):
                S = area(vectors[i], vectors[j], vectors[k])
                if S > max_area:
                    max_area = S
                    points = [vectors[i], vectors[j], vectors[k]]

    return max_area, points




sistema = [Vector(randint(-100, 100), randint(-100, 100), randint(-100, 100)) for i in range(100)]

print ('Max.area-->', maxarea(sistema)[0], '\n','Points of triangle-->',    *maxarea(sistema)[1])

print ('Center mass -->', centermass(sistema))

