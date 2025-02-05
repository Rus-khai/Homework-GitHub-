transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions_1, nam="USD"):
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    """
    if len(transactions_1) == 0:
        raise ValueError("Нет значений в списке")
    var = (
        transaction
        for transaction in transactions_1
        if transaction.get("operationAmount", []).get("currency", []).get("code", []) == nam
    )
    yield list(var)


usd_transactions = filter_by_currency(transactions, "USD")
for x in filter_by_currency(transactions, "USD"):
    print(next(usd_transactions))


def transaction_descriptions(transactions_1):
    """
    Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    if len(transactions_1) == 0:
        raise ValueError("Нет значений в списке")
    for transaction in transactions_1:
        yield transaction.get("description", [])


descriptions = transaction_descriptions(transactions)
for x in transaction_descriptions(transactions):
    print(next(descriptions))


def card_number_generator(start, stop):
    """
    который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    if start > stop:
        raise ValueError("некорректные значения")
    for number in range(start, stop):
        str_card_number = "0000" + " " + "0000" + " " + "0000" + " " + "000" + str(number)
        yield str_card_number


result = card_number_generator(1, 90000)
for card_number in card_number_generator(1, 6):
    print(next(result))
