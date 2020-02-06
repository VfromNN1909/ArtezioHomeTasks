# импортируем созданный нами пакет
# и из него импортируем нужный нам модуль
import website_alive.check_response as check_r

# адрес
site_url = str(input('Введите адрес сайта,который нужно проверить: '))
# получаем статус
result = check_r.check_status_code(site_url)
# проверяем
if result:
    print('Сайт доступен')
else:
    print('Сайт не доступен')
