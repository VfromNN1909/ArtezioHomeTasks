# импортируем регулярки
import re

# функция проверки пароля
def validate_password(password):
    # try на всякий,мало ли
    try:
        if re.match(r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w\d_*%&]{6,12}$', password):
            return True
    except:
        pass
    return False


print(validate_password('Vovkavl1900'))