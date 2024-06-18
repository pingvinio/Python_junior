system_str = input('''Введите F для перевода температуры из шкалы Цельсия в шкалу Фаренгейта или
введите C для перевода температуры из шкалы Фаренгейта в шкалу Цельсия - ''')
system = system_str.upper()
val_str = input('Введите нужное значение температуры - ') 
val = int(val_str)
def convert_temp(val, system):
    """Конвертирует температуру в нужную системы счисления

    Args:
        val: значение температуры
        system: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    if system == 'C':
        return print((val - 32) * 5/9)
    elif system == 'F':
        return print((9/5 * val) + 32)
    else:
        return print(val)
convert_temp (val, system)
