import json


def financial_transactions(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
    if not isinstance(data, list) or len(data) == 0 or len(data[0]) == 0:
        return []
    else:
        return data




