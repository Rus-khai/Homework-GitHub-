def filter_by_state(list_dict: list, state='EXECUTED') -> list:
    new_list = []
    for item in list_dict:
        if item['state'] == state:
            new_list.append(item)
    return new_list


def sort_by_date(dict_list_date: list) -> list:
    return sorted(dict_list_date, key=lambda k: k['date'], reverse=True)