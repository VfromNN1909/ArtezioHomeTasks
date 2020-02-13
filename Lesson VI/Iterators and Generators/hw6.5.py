# функция - генератор chain
# проходимся по всем-всем аргуметам
def chain(*args):
    for oarg in args:
        for iarg in oarg:
            yield iarg


# проверка
# 3 объекта итератора
i1 = iter([1, 2, 3, 4, 5])
i2 = iter([6, 7])
i3 = iter([8, 9])
# присваиваем
c = chain(i1, i2, i3)
# выводим
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
