import re
from database import read_transaction_csv
from collections import Counter


def search_description(list_transaction_dict, str_search):
    result_list_transaction = []
    pattern = re.compile(str_search)
    try:
        for transaction in list_transaction_dict:
            result = re.search(pattern, transaction.get('description', 'Перевод с карты на карту'))
            if result:
                result_list_transaction.append(transaction)
    except Exception as e:
        result_list_transaction = f'Ошибка {e}'
    finally:
        if result_list_transaction:
            return result_list_transaction
        return 'Операции не найдены'



# if __name__ == '__main__':
#     base_date = 'data/transactions.csv'
#     print(search_description(read_transaction_csv(base_date), 'счет'))

def quantity_transactions(list_transaction_dict, categories):
    descriptions = [transaction['description'] for transaction in list_transaction_dict]
    counter = Counter(descriptions)
    result_dict = {categories: counter[categories]}
    return result_dict





if __name__ == '__main__':
    base_date = 'data/transactions.csv'
    print(quantity_transactions(read_transaction_csv(base_date), 'Открытие вклада'))