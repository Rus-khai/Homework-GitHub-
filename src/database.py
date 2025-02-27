import csv
from typing import Any

import pandas as pd


def read_transaction_csv(base_date: Any):
    """Функция считывает csv.file и выводит список словарей с транзакциями"""
    with open(base_date, encoding='utf-8') as file:
        reader_data_csv = csv.DictReader(file, delimiter=';')
        result_list = []
        for data in reader_data_csv:
            result_list.append(data)
    return result_list

base_date = 'data/transactions.csv'
read_transaction_csv(base_date)


def read_transaction_excel(base_excel: Any):
    """Функция считывает excel.file и выводит список словарей с транзакциями"""
    df = pd.read_excel(base_excel)
    transactions_excel = df.to_dict(orient='records')
    return transactions_excel


base_excel = 'data/transactions_excel.xlsx'
read_transaction_excel(base_excel)
