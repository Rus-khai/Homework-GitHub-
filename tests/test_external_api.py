from unittest.mock import patch

from src.external_api import transaction_amount


@patch('requests.get')
def test_transaction_amount(mock_get):
    main_answer = [
        {
            "success": True,
            "query": {
                "from": "USD",
                "to": "RUB",
                "amount": 8221.37
            },
            "info": {
                "timestamp": 1739607724,
                "rate": 90.965376
            },
            "date": "2025-02-15",
            "result": 747860.013285
        }

    ]
    mock_get.return_value.json.return_value = main_answer

    transaction_amount(data)


data = \
        [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },
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
