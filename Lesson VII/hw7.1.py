# импортируем time
import time


# декоратор
def average_time(**value):
    def decorator(function):
        # тут будет храниться время
        totals = []

        def wrapper(*args, **kwargs):
            # итого времени
            total = 0
            # получаем значение из kwargs
            val = list(value.values())[0]
            # идем в цикле
            for i in range(val):
                # считаем время
                start = time.time()
                return_value = function(*args, **kwargs)
                end = time.time()
                total += round(int(end - start))
            nonlocal totals
            # переводим и засовываем в лист
            millisec = int(total * 1000)
            totals.append(millisec // val)
            # если мы вызывали функцию только один раз
            if len(totals) < 2:
                print('Среднее время работы:', int(totals[0]), 'мс')
            # если больше одного раза
            else:
                print('Среднее время работы:', (totals[-1] + totals[-2]) // val, 'мс')

            return return_value

        return wrapper

    return decorator


# функция
@average_time(n=2)
def foo(a):
    time.sleep(a)
    return a


# проверка
def main():
    a = foo(3)
    b = foo(7)
    c = foo(1)

    print(a, b, c)


main()
