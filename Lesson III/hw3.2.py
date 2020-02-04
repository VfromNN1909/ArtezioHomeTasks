# с рекурсией у меня как-то не сложилось
# поэтому я решил пойти, возможно
# более сложным путем


# функция, которая делает рассчеты
def foo(*args, **kwargs):
    # переводим все аргументы в строки
    s_args = str(args)
    s_kwargs = str(kwargs)
    # и парсим
    list_args = nums_from_string(s_args)
    list_kwargs = nums_from_string(s_kwargs)
    # получившиея числа складываем в один лист
    list_all = list_args + list_kwargs

    summa = 0  # сумма
    mult = 1  # произведение
    # счет
    for el in list_all:
        summa += el
        if el != 0:
            mult *= el
    # возвращаем результаты
    return summa, mult


# функция парсинга чисел из строк
def nums_from_string(string):
    length = len(string)
    nums = []
    i = 0
    while i < length:
        int_s = ''
        temp = string[i]
        while '0' <= temp <= '9':
            int_s += temp
            i += 1
            if i < length:
                temp = string[i]
            else:
                break
        i += 1
        if int_s != '':
            nums.append(int(int_s))
    return nums


# функция main, не обязательна, но
# для удобства и красоты, т.к. в программе
# больше 2ух функций
def main():
    print(
        foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])))


main()
