import abc, unittest
from math import sqrt, pi


# Абстрактная фигура
class Figure(abc.ABC):
    @abc.abstractmethod
    def square(self):
        pass


# Круг
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return pi * self.radius ** 2


# Треугольник
class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3
        if not (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            raise ValueError('Вы ввели  не ту фигуру!')

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self):
        t = sorted(list([self.a, self.b, self.c]))
        return bool(t[0] > 0 and t[0] * t[0] + t[1] * t[1] == t[2] * t[2])


def calculate_area(*args, **kwargs):
    if len(args) == 1:
        return Circle(*args).square()

    if len(args) == 3:
        return Triangle(*args).square()
    if len(args) > 3:
        raise NotImplementedError(
            "Метод расчета площади этой фигуры не реализован!"
        )


class CAD:
    @classmethod
    def square_all(cls, figures):
        for figure in figures:
            print(figure.square())




figures = [Triangle(4, 3, 5), Circle(5), ]
CAD.square_all(figures)
