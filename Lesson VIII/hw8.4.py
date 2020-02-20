# импортируем регулярки
import re

# функция проверки формата
def validate_iso(date):
    match_iso = re.findall(r'^(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)(\+|-)(\d\d):(\d\d)$', date)
    # try на всякий,мало ли
    try:
        if match_iso is not None:
            return True
    except:
        pass
    return False

# проверка
print(validate_iso('2020-01-30T01:45:36+11:22'))