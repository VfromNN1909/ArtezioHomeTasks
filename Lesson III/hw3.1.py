# функция возвращающая квадраты элементов
def first(arr):
    return list(map(lambda x: x * x, arr))


# функция возвращающая элементы на четных позициях
def second(arr):
    return list(arr[1::2])


# функция возвращающая кубы четных элементов на нечетных позициях
def third(arr):
    return list(
        map(lambda x: x * x * x, filter(lambda y: y % 2 == 0, arr[::2])))


# проверка работы программы
my_list = [int(el) for el in input().split()]
print(first(my_list), '\n', second(my_list), '\n', third(my_list))
