# создаем лист с помощью генератора
inp = list([str(i) for i in input().split()])  # вводится с клавиатуры
count = 0  # счетчик
for element in inp:
    if len(element) >= 2 and element[0] == element[-1]:
        count += 1
print(count)
