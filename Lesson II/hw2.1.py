# функция, считающая квадраты нечетных чисел
def squares(x):
    count = 0 # счетчик количества
    print('Квадраты нечетных чисел от 0 до х:')

    # идем до х в цикле
    for i in range(x): 
    	# и если число нечетное
        if i % 2 != 0:        	
        	# выводим его
            print('Число: ', i,', квадрат числа' , i, ':', i * i)
            count += 1 # и увеличиваем счетчик
    # выводим количесво с новой строки        
    print()
    print('Количество таких чисел: ', count)

# проверка работы программы
num = int(input('Введите х: '))
print(squares(num))