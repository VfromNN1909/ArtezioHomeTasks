# импорт
import requests


# функция делает запрос
# и возвращает объект
def make_a_request(url):
    response = requests.get(url)
    return response
