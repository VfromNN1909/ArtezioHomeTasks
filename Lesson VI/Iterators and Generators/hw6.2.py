# импортируем math просто для проверки
import math

# получаем все публичные аттрибуты и запихиваем их в лист
public_attibs = [attr for attr in dir(math) if attr[0] != '_']
# выводим
print(public_attibs)
