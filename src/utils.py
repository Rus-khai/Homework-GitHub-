import json


def financial_transactions(file_path):
    """функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    """
    with open(file_path, encoding="utf-8") as json_file:
        data_1 = json.load(json_file)
    if not isinstance(data_1, list) or len(data_1) == 0 or len(data_1[0]) == 0:
        return []
    else:
        return data_1


financial_transactions("../data/operations.json")
