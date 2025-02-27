import re
from database import read_transaction_csv


def search_description(list_transaction_dict, str_search):
    result_list_transaction = []
    pattern = re.compile(str_search)
    try:
        for transaction in list_transaction_dict:
            result = re.search(pattern, transaction.get('description', ''))
            if result:
                result_list_transaction.append(transaction)
    except Exception as e:
        result = f'Ошибка {e}'
    finally:
        if result_list_transaction:
            return result_list_transaction
        return 'Операции не найдены'



if __name__ == '__main__':
    base_date = 'data/transactions.csv'
    print(search_description(read_transaction_csv(base_date), 'cчет'))