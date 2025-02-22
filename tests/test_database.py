
from unittest.mock import patch

import pandas as pd

from src.database import read_transaction_csv


@patch('read_transaction_csv')
def test_database(mock_read_transaction_csv):  # Renamed mock for clarity
    mock_transactions = pd.read_csv[{'id': 3330422.0, 'state': 'EXECUTED', 'date': '2023-08-05T07:11:26Z', 'amount': 30065.0, 'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Mastercard 9458117363112215', 'to': 'Visa 6335859532296628', 'description': 'Перевод с карты на карту'}, {'id': 3794942.0, 'state': 'EXECUTED', 'date': '2021-05-24T02:37:49Z', 'amount': 14174.0, 'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Mastercard 8628645140673956', 'to': 'Счет 36990402090010935845', 'description': 'Перевод организации'}]

    mock_read_transaction_csv.return_value = mock_transactions

    result = read_transaction_csv('data/transactions.csv')

    mock_read_transaction_csv.assert_called_once_with('data/transactions.csv', delimiter=';')

    expected_result = mock_transactions.to_dict('records')
    assert result == expected_result


# @patch('src.database.read_transaction_csv')
# def test_read_transaction_excel(mock_get):
#     mock_transactions = {'id': 650703.0,
#                          'state': 'EXECUTED',
#                          'date': '2023-09-05T11:30:32Z',
#                          'amount': 16210.0,
#                          'currency_name': 'Sol',
#                          'currency_code': 'PEN',
#                          'from': 'Счет 58803664561298323391',
#                          'to': 'Счет 39745660563456619397',
#                          'description': 'Перевод организации'}
#
#     mock_get.return_value = mock_transactions
#     assert read_transaction_excel(base_excel) == mock_transactions
