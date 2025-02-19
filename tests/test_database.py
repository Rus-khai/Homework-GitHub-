from unittest.mock import patch

from src.database import base_date, base_excel, read_transaction_csv, read_transaction_excel


@patch('src.database.read_transaction_csv')
def test_database(mock_get):
    mock_transactions = \
        {'id': 650703.0,
         'state': 'EXECUTED',
         'date': '2023-09-05T11:30:32Z',
         'amount': 16210.0,
         'currency_name': 'Sol',
         'currency_code': 'PEN',
         'from': 'Счет 58803664561298323391',
         'to': 'Счет 39745660563456619397',
         'description': 'Перевод организации'}
    mock_get.return_value = mock_transactions
    assert read_transaction_csv(base_date) == mock_transactions


@patch('src.database.read_transaction_csv')
def test_read_transaction_excel(mock_get):
    mock_transactions = {'id': 650703.0,
                         'state': 'EXECUTED',
                         'date': '2023-09-05T11:30:32Z',
                         'amount': 16210.0,
                         'currency_name': 'Sol',
                         'currency_code': 'PEN',
                         'from': 'Счет 58803664561298323391',
                         'to': 'Счет 39745660563456619397',
                         'description': 'Перевод организации'}

    mock_get.return_value = mock_transactions
    assert read_transaction_excel(base_excel) == mock_transactions
