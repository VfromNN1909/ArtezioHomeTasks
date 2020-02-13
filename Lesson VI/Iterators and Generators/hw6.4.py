# функция циклического итератора
def cyclic_iterator(iterator):
    # лист
    endless_list = []
    # сначала заполняем лист
    for it in iterator:
        endless_list.append(it)
        yield it
    # счетчик
    counter = 0
    # потом зацикливаем
    while True:
        yield endless_list[counter]
        counter += 1
        if counter >= len(endless_list):
            # обнуляем счетчик
            counter = 0


# проверка
def main():
    li = [int(num) for num in range(5)]
    iterator = iter(li)
    cycle = cyclic_iterator(iterator)
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))


main()
