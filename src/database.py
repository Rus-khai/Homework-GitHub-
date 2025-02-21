from typing import Any

import pandas as pd


def read_transaction_csv(base_date: Any):
    """Функция считывает csv.file и выводит список словарей с транзакциями"""
    list_transaction_csv = []
    df = pd.read_csv(base_date, delimiter=';')
    transactions_csv = df.to_dict(orient='records')
    for transaction in transactions_csv:
        list_transaction_csv.append(transaction)
    return list_transaction_csv


base_date = 'data/transactions.csv'
print(read_transaction_csv(base_date))


def read_transaction_excel(base_excel: Any):
    """Функция считывает excel.file и выводит список словарей с транзакциями"""
    list_transaction_excel = []
    df = pd.read_excel(base_excel)
    transactions_excel = df.to_dict(orient='records')
    for transaction in transactions_excel:
        list_transaction_excel.append(transaction)
    return list_transaction_excel


base_excel = 'data/transactions_excel.xlsx'
read_transaction_excel(base_excel)
