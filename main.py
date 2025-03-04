from src.utils import financial_transactions
from src.database import read_transaction_csv, read_transaction_excel
from src.processing import filter_by_state, sort_by_date, filter_by_currency, filter_by_currency_for_csv
from src.search import search_description


print('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла)''')

user_input_file = str(input('Пользователь: '))
if user_input_file == '1':
    print('Для обработки выбран JSON-файл.')

elif user_input_file == '2':
    print('Для обработки выбран CSV-файл.')

elif user_input_file == '3':
    print('Для обработки выбран XLSX-файл')
else:
    print('Не верно выбрана категория')

print('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

user_input_filter = str(input('Пользователь:').upper())
if user_input_filter == 'EXECUTED' or user_input_filter == 'CANCELED' or user_input_filter == 'PENDING':
    print(f'Операции отфильтрованы по статусу "{user_input_filter}"')
else:
    print(f"Статус операции \"{user_input_filter}\" недоступен.")

print('Отсортировать операции по дате? Да/Нет')
user_sorted_date = str(input('Пользователь:').lower())
if user_sorted_date == 'да':
    print('Отсортировать по возрастанию или по убыванию?')
    user_sorted_INCREASING = str(input('Пользователь:').lower())
print('Выводить только рублевые транзакции? Да/Нет')
user_sorted_currency = str(input('Пользователь: ').lower())
print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
user_filter_list_transactions = str(input('Пользователь: ').lower())
if user_filter_list_transactions == 'да':
    user_filter_list_transactions_1 = str(input('Введите ключевое слово:').lower())
elif user_filter_list_transactions == 'нет':
    print('Распечатываю итоговый список транзакций...')



def main():
    if user_input_file == '1':
        result_json_list = financial_transactions('data/operations.json')
        if user_input_filter == 'EXECUTED' or user_input_filter == 'CANCELED' or user_input_filter == 'PENDING':
            result_filter_by_state = filter_by_state(result_json_list, user_input_filter)
            if user_sorted_date == 'да':
                if user_sorted_INCREASING == 'по убыванию':
                    result_sort_by_date = sort_by_date(result_filter_by_state, True)
                    if user_sorted_currency == 'да':
                        result_filter_by_currency = filter_by_currency(result_sort_by_date)
                        if user_filter_list_transactions == 'да':
                            result_search_description = search_description(result_filter_by_currency, user_filter_list_transactions_1)
                            return result_search_description
                        else:
                            return result_filter_by_currency
                    elif user_sorted_currency == 'нет':
                        if user_filter_list_transactions == 'да':
                            result_search_description = search_description(result_filter_by_state, user_filter_list_transactions_1)
                            return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_state

            elif user_sorted_date == 'нет':
                if user_sorted_currency == 'да':
                    result_filter_by_currency = filter_by_currency(result_filter_by_state)
                    if user_filter_list_transactions == 'да':
                        result_search_description = search_description(result_filter_by_currency,
                                                                       user_filter_list_transactions_1)
                        return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_currency
                elif user_sorted_currency == 'нет':
                    if user_filter_list_transactions == 'да':
                        result_search_description = search_description(result_filter_by_state,
                                                                       user_filter_list_transactions_1)
                        return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_state

    elif user_input_file == '2':
        result_csv_list = read_transaction_csv('data/transactions.csv')
        if user_input_filter == 'EXECUTED' or user_input_filter == 'CANCELED' or user_input_filter == 'PENDING':
            result_filter_by_state = filter_by_state(result_csv_list, user_input_filter)
            if user_sorted_date == 'да':
                if user_sorted_INCREASING == 'по убыванию':
                    result_sort_by_date = sort_by_date(result_filter_by_state, True)
                    if user_sorted_currency == 'да':
                        result_filter_by_currency = filter_by_currency_for_csv(result_sort_by_date)
                        if user_filter_list_transactions == 'да':
                            result_search_description = search_description(result_filter_by_currency,
                                                                           user_filter_list_transactions_1)
                            return result_search_description
                        else:
                            return result_filter_by_currency
                    elif user_sorted_currency == 'нет':
                        if user_filter_list_transactions == 'да':
                            result_search_description = search_description(result_filter_by_state,
                                                                           user_filter_list_transactions_1)
                            return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_state

            elif user_sorted_date == 'нет':
                if user_sorted_currency == 'да':
                    result_filter_by_currency = filter_by_currency_for_csv(result_filter_by_state)
                    if user_filter_list_transactions == 'да':
                        result_search_description = search_description(result_filter_by_currency,
                                                                       user_filter_list_transactions_1)
                        return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_currency
                elif user_sorted_currency == 'нет':
                    if user_filter_list_transactions == 'да':
                        result_search_description = search_description(result_filter_by_state,
                                                                       user_filter_list_transactions_1)
                        return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_state


    elif user_input_file == '3':
        result_excel_list = read_transaction_excel('data/transactions_excel.xlsx')
        if user_input_filter == 'EXECUTED' or user_input_filter == 'CANCELED' or user_input_filter == 'PENDING':
            result_filter_by_state = filter_by_state(result_excel_list, user_input_filter)
            if user_sorted_date == 'да':
                if user_sorted_INCREASING == 'по убыванию':
                    result_sort_by_date = sort_by_date(result_filter_by_state, True)
                    if user_sorted_currency == 'да':
                        result_filter_by_currency = filter_by_currency_for_csv(result_sort_by_date)
                        if user_filter_list_transactions == 'да':
                            result_search_description = search_description(result_filter_by_currency,
                                                                           user_filter_list_transactions_1)
                            return result_search_description
                        else:
                            return result_filter_by_currency
                    elif user_sorted_currency == 'нет':
                        if user_filter_list_transactions == 'да':
                            result_search_description = search_description(result_filter_by_state,
                                                                           user_filter_list_transactions_1)
                            return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_state

            elif user_sorted_date == 'нет':
                if user_sorted_currency == 'да':
                    result_filter_by_currency = filter_by_currency_for_csv(result_filter_by_state)
                    if user_filter_list_transactions == 'да':
                        result_search_description = search_description(result_filter_by_currency,
                                                                       user_filter_list_transactions_1)
                        return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_currency
                elif user_sorted_currency == 'нет':
                    if user_filter_list_transactions == 'да':
                        result_search_description = search_description(result_filter_by_state,
                                                                       user_filter_list_transactions_1)
                        return result_search_description
                    elif user_filter_list_transactions == 'нет':
                        return result_filter_by_state




print(main())














