"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)
'''
Ответ - 
3
3
потому что nonlocal вызывает перечисленные имена для обозначения ранее определенных переменных
в ближайшей области видимости, исключая глобальную. и далее меняет переменую number на 3 и первый раз выводит 3
второй раз print(number) выводитвторой раз 3 уже поменяную в функции(без nonlocal выводилось бы 9)
'''
