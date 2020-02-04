# попытался писать максимально кратко
# функция находит элемент, который
# максимально приближен к нулю
# относительно других элементов
def m(s):
    c=s.split()
    v=[]
    for i in c:
        v.append(abs(float(i)))
    return c[v.index(min(v))]

s = input()
print(m(s))