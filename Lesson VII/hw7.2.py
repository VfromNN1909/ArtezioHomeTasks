# с заданием не справился
# стабильно выводит "0 мс"
# как-то не пошло у меня с декораторами классов ;(
# но я старался :)

# импортируем time
import time


# функция возвращающая список методов
def get_methods(class_name):
    return [func for func in dir(class_name) if callable(getattr(class_name, func)) and not func.startswith("__")]


# собственно сам декоратор
def time_methods(*method_names):
    def decorator(specific_class):
        # тут я попытался в цикле пройтись по заданным методам
        for method in method_names:
            # если таковой имеется в списке емтодов класса
            if method in get_methods(specific_class):
                # то замеряем время
                def wrapper(self, *args, **kwargs):
                    # тут я пытался в цикле
                    start = time.time()
                    return_value = specific_class(self, *args, **kwargs)
                    end = time.time()
                    total = end - start
                    print("{} мс".format(total * 1000))
                    return return_value
        return wrapper

    return decorator


# класс
@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s

    def inspect(self):
        time.sleep(self.s)

    def foo(self):
        return self.s

# проверка
def main():
    a = Spam(6)
    a.inspect()
    a.foo()


main()
