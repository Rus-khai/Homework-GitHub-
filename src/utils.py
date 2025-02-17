import json


def financial_transactions(file_path):
    """ функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(file_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


print(financial_transactions('../data/operations.json'))
