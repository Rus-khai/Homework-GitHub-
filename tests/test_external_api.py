from unittest.mock import patch

import src.external_api


@patch('requests.get')
def test_transaction_amount(mock_get):
    main_answer = {
                   'success': True,
                   'query': {'from': 'USD', 'to': 'RUB', 'amount': 9824.07},
                   'info': {'timestamp': 1739783716, 'rate': 91.569771},
                   'date': '2025-02-17',
                   'result': 899587.840188
                  }
    mock_get.return_value.json.return_value = main_answer

    assert src.external_api.transaction_amount(data) == round(main_answer.get("result", 0), 2)


data = {
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
       }
