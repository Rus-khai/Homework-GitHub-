from typing import Any

import pandas as pd


def read_transaction_csv(base_date: Any):
    """Функция считывает csv.file и выводит список словарей с транзакциями"""
    df = pd.read_csv(base_date, delimiter=';')
    transactions_csv = df.to_dict(orient='records')
    for transaction in transactions_csv:
        return transaction


base_date = 'data/transactions.csv'
read_transaction_csv(base_date)


def read_transaction_excel(base_excel: Any):
    """Функция считывает excel.file и выводит список словарей с транзакциями"""
    df = pd.read_excel(base_excel)
    transactions_excel = df.to_dict(orient='records')
    for transaction in transactions_excel:
        return transaction


base_excel = 'data/transactions_excel.xlsx'
print(read_transaction_excel(base_excel))
