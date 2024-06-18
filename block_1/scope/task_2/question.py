"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
'''
ответ -
Test message
None
потому что transmit_to_space("Test message") даёт вывод сообщения Test message,
а последующая функция print() выводит None так как нет парамметров вывода
'''
