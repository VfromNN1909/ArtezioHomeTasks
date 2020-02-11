# класс Observable
class Observable:
    # конструктор
    def __init__(self, **kwargs):
        for kwarg in kwargs:
            self.__dict__[kwarg] = kwargs[kwarg]
    # переопределение print()
    def __str__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(
                '{}={}'.format(key, val)
                for key, val in self.__dict__.items() if not key.startswith('_')
            )
        )

# наследуемся от Observable
class X(Observable):
    pass

# проверяем
x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(x)