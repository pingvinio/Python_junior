month_enter = input('''Введите название месяца - ''')

def month_day(month_enter):
    """Возвращает количество дней по месяцу

    Args:
        month_enter: название месяца

    Returns: количество дней
    """
    raise NotImplementedError
month_dict = {'январь': 1, 'февраль': 2, 'март': 3,
               'апрель': 4, 'май': 5, 'июнь': 6,
               'июль': 7, 'август': 8, 'сентябрь': 9,
               'октябрь': 10, 'ноябрь': 11, 'декабрь': 12,}
    month = month_dict.get(month_enter.lower())
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return print('31 день')
    elif month in [4, 6, 9, 11]:
        return print('30 дней')
    elif month == 2:
        return print('28 или 29 дней')
    else:
        return print(0)
month_day(month_enter)
