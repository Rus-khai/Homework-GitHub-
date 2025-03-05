import csv
import os
from typing import Any

import pandas as pd

from config import DATA_DIR

file_path_csv = os.path.join(DATA_DIR, 'transaction.csv')
file_path_excel = os.path.join(DATA_DIR, 'transactions_excel.xlsx')


def read_transaction_csv(base_date_1: Any):
    """Функция считывает csv.file и выводит список словарей с транзакциями"""
    with open(base_date_1, encoding='utf-8') as file:
        reader_data_csv = csv.DictReader(file, delimiter=';')
        result_list = []
        for data in reader_data_csv:
            result_list.append(data)
    return result_list


# read_transaction_csv(file_path_csv)


def read_transaction_excel(file_path_excel: Any):
    """Функция считывает excel.file и выводит список словарей с транзакциями"""
    reader_data_excel = pd.read_excel(file_path_excel)
    result = reader_data_excel.to_dict(orient='records')
    return result


# read_transaction_excel('data/transactions_excel.xlsx')
