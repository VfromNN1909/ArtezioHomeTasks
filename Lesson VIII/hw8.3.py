# ! --- КОТИК НЕ ПОТЕРЯЛ НИ ЕДИНОГО ПИКСЕЛЯ --- !

# сначала пытался сделать с полным путем до файла
# но ПЧ что-то ругался
# поэтому просто закинул картинку в папку venv

# импортируем нужные библиотеки
import pathlib
import requests
import base64
import os


# функция запроса
def cat_transfer(filepath, targername):
    # запрос
    response = requests.post("https://postman-echo.com/post",
                             files={filepath: open(filename, 'rb')})
    # получаем octet-stream
    pic = response.json()['files'][filename][len('data:application/octet-stream;base64,'):]
    # создаем из него файл .jpeg
    with open(targername, 'wb') as postkotik_file:
        postkotik_file.write(base64.b64decode(pic))
    # возвращаем размер
    return os.path.getsize(targername)


# проверка
filename = 'kotik.jpeg'
targername = input('Введите название картинки: ')

size = cat_transfer(filename, targername + '.jpeg')
print(size, 'bytes')
