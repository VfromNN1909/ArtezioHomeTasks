# логин и пароль
log = 'admin'
pas = '1337'

# переменная для выхода из цикла
flag = True

# пока flag = True
while flag:
	# ввод логина и пароля
    input_log = input('Введите логин: ')
    input_pas = input('Введите пароль: ')
    # если логин и пароль совпадают
    if input_log == log and input_pas == pas:
    	# то выводим,что всё хорошо
        print('Password for user:', input_log, 'is correct')
        # и выходим из цикла
        flag = False; # можно было бы сделать с оператором break, но это не очень хороший тон программирования
    # иначе,если логин или пароль не верны
    elif input_log != log or input_pas != pas:
    	# то выводим,что они не верны
        print('Password or login for user:', input_log, 'is incorrect')
        # и просим повторить попытку
        print('Please try again...')
