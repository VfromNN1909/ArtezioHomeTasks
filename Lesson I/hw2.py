# импортируем Counter
from collections import Counter

# читаем строку с клавиатуры
s = input('Enter your string: ')

# засовываем строку в Counter
c = Counter(s)

# выводим
print(c)
