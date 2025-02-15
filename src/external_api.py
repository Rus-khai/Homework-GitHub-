import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')


API_KEY = os.getenv('API_KEY')
payload = {}
headers = {"apikey": API_KEY}
code_RUB = 'RUB'


def transaction_amount(transactions):
    """
    функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    """
    for transaction in transactions:
        if (transaction.get('operationAmount').get('currency').get('code') == 'USD' or
                transaction.get('operationAmount').get('currency').get('code') == 'EUR'):
            url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
                   f"{code_RUB}&from="f"{transaction.get('operationAmount').get('currency').get('code')}&amount="
                   f"{transaction.get('operationAmount').get('amount')}")
            response = requests.request("GET", url, headers=headers)

            result = response.text
            return result
        else:
            result = transaction.get('operationAmount').get('amount')
            return result


data = \
        [

            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {
                    "amount": "48223.05",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 41421565395219882431"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            }]


print(transaction_amount(data))
