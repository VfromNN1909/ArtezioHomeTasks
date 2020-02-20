# импортируем requests
import requests

# получаем результат
doc = requests.get('https://vk.com').text
# выводим длинну
print(len(doc))
