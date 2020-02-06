# импортируем модуль с функцией запроса
import website_alive.make_request as make_r


# функция проверяет статус сайта
def check_status_code(url):
    response_obj = make_r.make_a_request(url)
    # если статус = 200 - True
    # иначе - False
    return response_obj.status_code == 200
