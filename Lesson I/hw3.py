# функция fast
# fast - F-irst + l-AST
def fast(s):
    if len(s) < 2:
        return "Empty string"
    elif len(s) == 2:
        return s * 2
    else:
        return s[:2] + s[-2::1]


# проверка функции
s = input('Enter your string: ')
print(fast(s))
