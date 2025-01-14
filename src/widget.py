from masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    number_card = ''
    type_card = ''
    for char in info_card:
        if char.isdigit():
            number_card += char
        elif char.isalpha():
            type_card += char
    if len(number_card) <= 16:
        mask_card = get_mask_card_number(number_card)
    else:
        mask_card = get_mask_account(number_card)

    return type_card + " " + mask_card


def get_date(date: str) -> str:
    filter_date = date[:10].split('-')
    reversed_filter_date = filter_date[::-1]
    str_reversed_filter_date = str(reversed_filter_date[0]
                                   + '.' + reversed_filter_date[1]
                                   + '.' + reversed_filter_date[2])
    return str_reversed_filter_date
