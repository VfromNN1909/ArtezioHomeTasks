# класс
class Student:
    # конструктор
    def __init__(self, name, conf):
        # имя
        self.name = name
        # словарь
        self.conf = conf
        # лабы
        self.labs = [0] * self.conf.get('lab_num')
        # экзамен
        self.exam = 0
    # функция для сдачи лаб
    def make_lab(self, m, n = -1):
        if n >= self.conf.get('lab_num'):
            return self
        if n == -1:
            try:
                n = self.labs.index(0)
            except:
                return self

        if m > self.conf.get('lab_max'):
            m = self.conf.get('lab_max')

        self.labs[n] = m

        return self
    # функция для сдачи экзамена
    def make_exam(self, m):
        if m > self.conf.get('exam_max'):
            m = self.conf.get('exam_max')
        self.exam = m
        return self
    # проверка сертификата
    def is_certified(self):
        marks_sum = sum(self.labs) + self.exam
        is_cert = False
        if float(marks_sum / 100) >= self.conf.get('k'):
            is_cert = True
        elif float(marks_sum / 100) >= self.conf.get('k'):
            is_cert = False
        return (marks_sum, is_cert)
# функция main
def main():
    # проверка
    s1 = Student('Vladimir' , {
        'exam_max' : 30,
        'lab_max' : 6,
        'lab_num' : 5,
        'k' : 0.6
    })
    print(s1.is_certified())

    s2 = Student('Vasily', {
        'exam_max' : 30,
        'lab_max' : 45,
        'lab_num' : 5,
        'k' : 0.6
    })
    s2.make_lab(60)
    print(s2.is_certified())
# запускаем
main()