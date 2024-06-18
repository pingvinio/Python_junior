int = 0
def counter(function):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    def wrapper():
        global int
        result = function()
        int += 1
        return int
    return wrapper
