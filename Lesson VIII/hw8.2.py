# импортируем requests
import requests


# функция конвертации
def convert(amount, curr, converted_money):
    # url
    url = 'https://api.exchangerate-api.com/v4/latest/{}'.format(curr)
    # запрос
    response = requests.get(url)
    # получаем json
    data = response.json()
    # считаем результат
    return amount * data['rates'][converted_money]


# проверка
# вводим
amount = float(input('Введите количество денег: '))
curr = str(input('Введите валюту, которую хотите конвертировать: '))
converted_money = str(input('Введите целевую валюту: '))
# печатаем
print(convert(amount, curr, converted_money))
