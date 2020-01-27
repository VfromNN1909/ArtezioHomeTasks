# вводим число
num = int(input('Enter your number: '))

# с помощью генератора присваиваем значения словарю 
dic = {x : x ** 2 for x in range(1, num + 1)}

# выводим результат
print(dic)
