# функция деления
def is_devide(a, b, c):
    count = 0  # счетчик
    # перебираем значения между a и b
    for i in range(a + 1, b):
        # если число делится на с
        if i % c == 0:
            count += 1  # то увеличиваем счетчик
    # возвращаем количество таких чисел
    return count


# проверка работы программы
print('Введите числа a, b, c:')
a = int(input('a - '))
b = int(input('b - '))
c = int(input('c - '))
print('Количество чисел: ', is_devide(a, b, c))
