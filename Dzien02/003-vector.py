
# Użycie magicznych metod

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[ {self.x}, {self.y} ]"

    def add_vector(self, other_vector):
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector(x, y)

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y

    def __sub__(self, obj):
        x = self.x - obj.x
        y = self.y - obj.y
        return Vector(x, y)

    def __add__(self, obj):
        if type(obj) is Vector:
            x = self.x + obj.x
            y = self.y + obj.y
            return Vector(x, y)
        if type(obj) in [int, float]:
            return Vector(self.x + obj, self.y + obj)
        if type(obj) in [list, tuple] and len(obj)==2:
            return Vector(self.x+obj[0], self.y+obj[1])
        raise TypeError()

class SuperVector(Vector):

    def add_vector(self, other_vector):
        v = super(SuperVector, self).add_vector(other_vector)
        v.x, v.y = -1*v.x, -1*v.y
        return v

########
wektor1 = Vector(2,3)
print(wektor1)

wektor2 = Vector(2,3)
print(wektor1)

superwektor1 = SuperVector(2,2)
superwektor2 = SuperVector(3,3)
print(superwektor1.add_vector(superwektor2))


try:
    # kod do wykonania który może dać wyjątek
    print(wektor1 + "abc")
    j = 1/0
except TypeError as exc:
    print("Coś nie tak z typem zmiennej", exc)
except ZeroDivisionError as exc:
    print("proba dzielenie przez zero",exc)
except Exception as exc:
    print("coś poszło nie tak",exc)
else:
    # wykona się tylko gdy nie bedzie wyjatku
    print("wykonam się, gdy nie bedzie wyjątku")
finally:
    print("Zawsze wykonane")

print(wektor1 == wektor2)

print(wektor1.add_vector(wektor2))
print(wektor1 + wektor2)
print(wektor1 + 3.5)
print(wektor1 + [1,2])
print(wektor1 + (1,2))

