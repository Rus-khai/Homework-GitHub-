from masks import get_mask_account, get_mask_card_number
from typing import Any


def mask_account_card(info_card: Any) -> Any:
    """
    Функция принимает и обрабатывать информацию как о картах, так и о счетах и маскирует её
    """
    number_card = ""
    type_card = ""
    for symbol in info_card:
        if symbol.isdigit():
            number_card += symbol
        elif symbol.isalpha():
            type_card += symbol
    if len(number_card) <= 16:
        mask_card = get_mask_card_number(number_card)
    else:
        mask_card = get_mask_account(number_card)

    return type_card + " " + mask_card


def get_date(date: Any) -> Any:
    """
    функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024").
    """
    filter_date = date[:10].split("-")
    reversed_filter_date = filter_date[::-1]
    str_reversed_filter_date = str(
        reversed_filter_date[0] + "." + reversed_filter_date[1] + "." + reversed_filter_date[2]
    )
    return str_reversed_filter_date
