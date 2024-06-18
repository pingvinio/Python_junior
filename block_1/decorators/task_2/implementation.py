from block_1.common import (
    factorial,
    MyException,
)

def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(num):
        if type(num) == int and num >= 0:
            result = function(num)
            return result
        else:
            raise MyException(Exception)

    return wrapper
