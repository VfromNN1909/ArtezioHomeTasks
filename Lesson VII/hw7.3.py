# декоратор
def curry(func):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return (lambda *args2, **kwargs2:
                curried(*(args + args2), **dict(kwargs, **kwargs2)))

    return curried


# функция
@curry
def foo(a, b, c, d, e):
    return a + b + c + d + e


# проверка
def main():
    print(foo(1)(2)(3)(4)(5))


main()
