from src.database import read_transaction_csv, read_transaction_excel
from src.processing import filter_by_currency, filter_by_currency_for_csv, filter_by_state, sort_by_date
from src.search import search_description
from src.utils import financial_transactions
from src.widget import get_date, mask_account_card


def main():
    """
    функция main отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла)''')
    result_list = None
    user_input_file = str(input('Пользователь:'))
    while user_input_file != '1' or user_input_file != '2' or user_input_file != '3':
        if user_input_file == '1':
            print('Для обработки выбран JSON-файл.')
            result_list = financial_transactions('data/operations.json')
            break
        elif user_input_file == '2':
            print('Для обработки выбран CSV-файл.')
            result_list = read_transaction_csv('data/transactions.csv')
            break
        elif user_input_file == '3':
            print('Для обработки выбран XLSX-файл')
            result_list = read_transaction_excel('data/transactions_excel.xlsx')
            break
        user_input_file = str(input('Не правильная категория. Выберите правильную категорию:'))

    print('''Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    user_input_filter = str(input('Пользователь:').upper())
    while user_input_filter != 'EXECUTED' or user_input_filter != 'CANCELED' or user_input_filter != 'PENDING':
        if user_input_filter == 'EXECUTED' or user_input_filter == 'CANCELED' or user_input_filter == 'PENDING':
            print(f'Операции отфильтрованы по статусу "{user_input_filter}"')
            result_list = filter_by_state(result_list, user_input_filter)
            break
        user_input_filter = str(input(f'Статус операции \"{user_input_filter}\" недоступен. '
                                      f'Введите статус, по которому необходимо выполнить фильтрацию. '
                                      f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:').upper())
    print('Отсортировать операции по дате? Да/Нет')
    user_sorted_date = str(input('Пользователь:').lower())
    while user_sorted_date != 'да' or user_sorted_date != 'нет':
        if user_sorted_date == 'да':
            print('Отсортировать по возрастанию или по убыванию?')
            user_sorted_INCREASING = str(input('Пользователь:').lower())
            while user_sorted_INCREASING != 'по возрастанию' or user_sorted_INCREASING != 'по убыванию':
                if user_sorted_INCREASING == 'по убыванию':
                    result_list = sort_by_date(result_list, True)
                    print(f'Идёт фильтрация по "{user_sorted_INCREASING}"...')
                    break
                elif user_sorted_INCREASING == 'по возрастанию':
                    result_list = sort_by_date(result_list, False)
                    print(f'Идёт фильтрация по "{user_sorted_INCREASING}"...')
                    break
                user_sorted_INCREASING = str(input('Не правильный ввод. '
                                                   'Введите по убыванию или по возрастанию:').lower())
            break
        elif user_sorted_date == 'нет':
            break
        user_sorted_date = str(input('Не правильный ввод. Введите да или нет:').lower())

    print('Выводить только рублевые транзакции? Да/Нет')
    user_sorted_currency = str(input('Пользователь:').lower())
    while user_sorted_currency != 'да' or user_input_filter != 'нет':
        if user_sorted_currency == 'да':
            print('Идёт фильтрация...')
            if user_input_file == '2' or user_input_file == '3':
                result_list = filter_by_currency_for_csv(result_list)
                break
            elif user_input_file == '1':
                result_list = filter_by_currency(result_list)
                break
        elif user_input_filter == 'нет':
            break

        user_sorted_currency = str(input('Не правильный ввод. Введите да или нет:').lower())

    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    user_filter_list_transactions = str(input('Пользователь: ').lower())
    while user_filter_list_transactions != 'да' or user_filter_list_transactions != 'нет':
        if user_filter_list_transactions == 'да':
            user_filter_list_transactions_1 = str(input('Введите ключевое слово:').lower())
            result_list = search_description(result_list, user_filter_list_transactions_1)
            break
        if user_filter_list_transactions == 'нет':
            break
        user_filter_list_transactions = str(input('Не правильный ввод. Введите да или нет:').lower())

    print('Распечатываю итоговый список транзакций...')
    if len(result_list) > 0:
        print(f'Всего банковских операций в выборке: {len(result_list)}')
    else:
        print('Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

    if user_input_file == '1':
        for transaction in result_list:
            print(f'{get_date(transaction.get('date'))} {transaction.get('description')}\n'
                  f'{mask_account_card(transaction.get('from', ''))} -> '
                  f'{mask_account_card(transaction.get('to', ''))}\n'
                  f'{transaction.get('operationAmount').get('amount')} '
                  f'{transaction.get('operationAmount').get('currency').get('name')}')
    else:
        for transaction in result_list:
            print(f'{get_date(transaction.get('date'))} {transaction.get('description')}\n'
                  f'{mask_account_card(transaction.get('from', ''))} -> '
                  f'{mask_account_card(transaction.get('to', ''))}\n'
                  f'{transaction.get('amount')} {transaction.get('currency_code')}')


main()
