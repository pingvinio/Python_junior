from math import factorial
import time
def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(fun):
        time_start = time.time()
        result = function(fun)
        time_stop = time.time()
        print(f"Функция выполнилась за - {time_stop - time_start} секунд")
        return result

    return wrapper

#Проверка
@time_execution
def fact(numb):  
   return factorial(numb)
print(fact(33))
