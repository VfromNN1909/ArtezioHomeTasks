# импортируем sqrt
from math import sqrt


# класс наследуется от объекта
class Complex(object):
    # конструктор
    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    # вывод
    def __str__(self):
        # чтобы не было "число"+-"число"
        if self.imag < 0:
            return "{}-{}i".format(round(self.real, 2), round(abs(self.imag), 2))
        else:
            return "{}+{}i".format(round(self.real, 2), round(self.imag, 2))

    # сложение
    def __add__(self, other):
        return Complex(float(self.real) + float(other.real),
                       float(self.imag) + float(other.imag))

    # вычитание
    def __sub__(self, other):
        return Complex(float(self.real) - float(other.real),
                       float(self.imag) - float(other.imag))

    # умножение
    def __mul__(self, other):
        return Complex((float(self.real) * float(other.real) - float(self.imag * other.imag)),
                       (float(self.real) * float(other.imag) + float(self.imag) * float(other.real)))

    # деление
    def __truediv__(self, other):
        return Complex(float(self.real * other.real + self.imag * other.imag)
                       / float(other.real ** 2 + other.imag ** 2), float(
            self.imag * other.real - self.real * other.imag) / float(
            other.real ** 2 + other.imag ** 2))

    # модуль
    def __abs__(self):
        return Complex(sqrt(self.real ** 2 + self.imag ** 2), 0.00)


# main для красоты и понятности
def main():
    # вводятся 2 листа
    arr1 = list(input().split())
    arr2 = list(input().split())
    # берем числа из листов
    c1 = Complex(arr1[0], arr1[1])
    c2 = Complex(arr2[0], arr2[1])
    # выводим результат
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print(abs(c1))
    print(abs(c2))


main()