import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')


API_KEY = os.getenv('API_KEY')
payload = {}
headers = {"apikey": API_KEY}
code_RUB = 'RUB'


def transaction_amount(transaction):
    """
    функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    """
    if (transaction.get('operationAmount').get('currency').get('code') == 'USD' or
            transaction.get('operationAmount').get('currency').get('code') == 'EUR'):
        url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
               f"{code_RUB}&from="f"{transaction.get('operationAmount').get('currency').get('code')}&amount="
               f"{transaction.get('operationAmount').get('amount')}")
        response = requests.request("GET", url, headers=headers)

        result = response.json()
        return round(result.get('result'), 2)
    else:
        result = transaction.get('operationAmount').get('amount')
        return result


data = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
                        }
                            }
        }


print(transaction_amount(data))