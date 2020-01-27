# вводим три множества с клавиатуры
a = set(input().split())
b = set(input().split())
c = set(input().split())

# выводим результат
print(c.issubset(a) and c.issubset(b))
