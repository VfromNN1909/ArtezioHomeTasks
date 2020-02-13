# импортируем json,дабы красиво вывести словарь
import json

# для генерации значений
# если ввести значение < количество ключей + 1(27)
# то вместо недостающих значений будет None
# если ввести больше,то лишние значения будут игнорироваться
limit = int(input('Введите лимит: '))

# генерируем ключи - буквы от a до z
keys = [chr(int(i)) for i in range(ord('a'), ord('z') + 1)]
# генерируем ключи - числа от 1 до limit'а
vals = [int(i) for i in range(1, limit)]
# словарь - результат
res = {}
# слияние 2ух листов в словарь
[res.update({keys[i]: vals[i]}) if i < len(vals) else res.update({keys[i]: None}) for i in range(len(keys))]
# красиво выводим словарь
print(json.dumps(res, indent=1))
