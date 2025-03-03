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



