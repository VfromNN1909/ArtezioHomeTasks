# количество пар значений
T = int(input())
# получаем пару каждую итерацию
for i in range(T):
    a, b = input().split()
    # и пытаемся поделить
    try:
        print(int(a) // int(b))
    # если что выводим ошибку
    except Exception as ex:
        print('Error Code:', ex)
