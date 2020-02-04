# функция, которая считает среднее арифметическое
# и находит максимум из 4ех чисел


def foo(first_num, second_num, third_num, fourth_num):
    return ((first_num + second_num + third_num + fourth_num) / 4,
            max(first_num, second_num, third_num, fourth_num))


current_max = 0  # текущее максимальное
count = 0  # счетчик

# бесконечный цикл
# для выхода из него
# нужно ввести больше или меньше 4ех чисел
while True:
    # ввод через лист для удобства
    print('Введите 4 числа через пробел: ')
    nums = [int(el) for el in input().split()]
    # собственно условие выхода из цикла
    if len(nums) != 4:
        break
    a = nums[0]
    b = nums[1]
    c = nums[2]
    d = nums[3]
    # считаем
    mean, maximum = foo(a, b, c, d)
    if count == 0:
        print(mean, maximum)
        current_max = maximum
    elif maximum > current_max and count > 0:
        current_max = maximum
        print(mean, current_max)
    else:
        print(mean, current_max)
    count += 1