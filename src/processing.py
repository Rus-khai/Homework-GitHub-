from typing import Union


def filter_by_state(list_of_data: Union[list], state: Union[str] = "EXECUTED") -> Union[list]:
    """
    Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'), и возвращает новый список словарей,
    у которых ключ state соответствует указанному значению
    """
    if not isinstance(list_of_data, list):
        raise TypeError("Не правильный тип данных")
    filter_data_list = []
    for data_dictionary in list_of_data:
        if data_dictionary.get("state", 0) == state:
            filter_data_list.append(data_dictionary)
    return filter_data_list


def sort_by_date(dict_list_date: Union[list], direction=True) -> Union[list]:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание),
    и возвращать новый список, отсортированный по дате (date)
    """
    return sorted(dict_list_date, key=lambda k: k["date"], reverse=direction)


def filter_by_currency(list_transactions):
    """
    Функция принимает список словарей, и возвращает новый список словарей,
    у которых ключа code соответствует указанному значению
    """
    if not isinstance(list_transactions, list):
        raise TypeError("Не правильный тип данных")
    filter_data_list = []
    for list_transaction in list_transactions:
        if list_transaction.get('operationAmount').get('currency').get('code') == 'RUB':
            filter_data_list.append(list_transaction)
    return filter_data_list


def filter_by_currency_for_csv(list_transactions):
    """
    Функция принимает список словарей, и возвращает новый список словарей,
    у которых ключа currency_code соответствует указанному значению
    """
    if not isinstance(list_transactions, list):
        raise TypeError("Не правильный тип данных")
    filter_data_list = []
    for list_transaction in list_transactions:
        if list_transaction.get('currency_code') == 'RUB':
            filter_data_list.append(list_transaction)
    return filter_data_list
