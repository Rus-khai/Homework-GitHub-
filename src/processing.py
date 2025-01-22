from typing import Union


def filter_by_state(list_of_data: Union[list], state: Union[str] = "EXECUTED") -> Union[list]:
    """
    Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'), и возвращает новый список словарей,
    у которых ключ state соответствует указанному значению
    """
    filter_data_list = []
    for data_dictionary in list_of_data:
        if data_dictionary["state"] == state:
            filter_data_list.append(data_dictionary)
    return filter_data_list


def sort_by_date(dict_list_date: Union[list]) -> Union[list]:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание),
    и возвращать новый список, отсортированный по дате (date)
    """
    return sorted(dict_list_date, key=lambda k: k["date"], reverse=True)
