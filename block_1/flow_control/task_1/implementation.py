def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    item_list = []
    for item in range(1000, 2000):
        if item % 7 == 0 and item % 5 != 0:
            item_list.append(item)
    return print(item_list)
get_numbers()
