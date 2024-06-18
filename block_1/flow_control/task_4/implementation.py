from datetime import timedelta
import datetime
date_str = input('Введите дату - ')
date_input = datetime.datetime.strptime(date_str, '%Y%m%d').date()
def get_next_day(date_input):
    """Возвращает следующую дату для заданной

    Args:
        next_day: определенная исходная дата

    Returns: следующая дата
    """
try:
        next_day = date_input + timedelta(days=1)
        return print(next_day)
    except:
        return print('Что-то пошло не так!!!')
get_next_day(date_input)
