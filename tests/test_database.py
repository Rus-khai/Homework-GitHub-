import unittest.mock

from src.database import read_transaction_csv, read_transaction_excel


@unittest.mock.patch('pandas.read_csv')
def test_database(get_mock):
    mock_transaction = [{'id': 3330422.0,
                         'state': 'EXECUTED',
                         'date': '2023-08-05T07:11:26Z',
                         'amount': 30065.0,
                         'currency_name': 'Ruble',
                         'currency_code': 'RUB',
                         'from': 'Mastercard 9458117363112215',
                         'to': 'Visa 6335859532296628',
                         'description': 'Перевод с карты на карту'}]

    get_mock.return_value.to_dict.return_value = mock_transaction
    assert read_transaction_csv('data/transactions.csv') == mock_transaction


@unittest.mock.patch('pandas.read_excel')
def test_read_transaction_excel(mock_get):
    mock_transactions = [{'id': 3330422.0,
                          'state': 'EXECUTED',
                          'date': '2023-08-05T07:11:26Z',
                          'amount': 30065.0,
                          'currency_name': 'Ruble',
                          'currency_code': 'RUB',
                          'from': 'Mastercard 9458117363112215',
                          'to': 'Visa 6335859532296628',
                          'description': 'Перевод с карты на карту'}]

    mock_get.return_value.to_dict.return_value = mock_transactions
    assert read_transaction_excel('data/transactions_excel.xlsx') == mock_transactions
