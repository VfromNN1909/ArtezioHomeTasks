# элементы на четных позициях - имеется ввиду натуральные числа
# то есть отчет с единицы, и на четных позициях находятся элементы 2, 4, 6, 8

# класс итератор
class EvenIterator(object):
    # конструктор
    def __init__(self, collection):
        # счетчик
        self.counter = 0
        # лист
        self.collection = collection

    # имплементируем __iter__
    def __iter__(self):
        return self

    # имплементируем __next__
    def __next__(self):
        # если не дошли до конца коллекции
        if self.counter < len(self.collection):
            # плюсуем
            self.counter += 2
            return self.counter
        # иначе вызываем StopIteration
        else:
            raise StopIteration


# проверка
def main():
    itr = EvenIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))  # вызовется StopIteration


main()
