# импортируем регулярки
import re


# функция проверки пароля
def validate_sentence(password):
    # try на всякий,мало ли
    try:
        if re.findall(r'[[a-zA-Z {2,}]{4,}]*\?', string) is not None:
            return True
    except:
        pass
    return False


# проверка
string = 'aa aa aa f h saa aa aga aa aa?'

print(validate_sentence(string))
