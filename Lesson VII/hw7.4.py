# декоратор
def accepts(*types):
    def check_accepts(function):
        # проверяем совпадение количества
        if len(types) != function.__code__.co_argcount:
            raise AttributeError

        # проверяем типы
        def new_function(*args, **kwds):
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    # если не совпадают
                    # то выводим сообщение
                    print("Несовпадение переданных аргументов!")
                    # и поднимаем ошибку
                    raise TypeError
            # возвращаем значения
            return function(*args, **kwds)

        return new_function

    return check_accepts


# функция
@accepts(int, (int))
def func(arg1, arg2):
    return arg1 * arg2


# проверка
def main():
    print(func(3, 2))  # -> 6
    print(func("three"))  # -> TypeError


main()
