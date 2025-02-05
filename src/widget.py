from typing import Any, Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: Any) -> Any:
    """
    Функция принимает и обрабатывать информацию как о картах, так и о счетах и маскирует её
    """
    number_card = ""
    type_card = ""

    for symbol in info_card:
        if symbol.isdigit():
            break
        else:
            type_card += symbol
    for symbol in info_card:
        if symbol.isdigit():
            number_card += symbol
    if len(number_card) > 16:
        mask_card = get_mask_account(number_card)
    else:
        mask_card = get_mask_card_number(number_card)
    return type_card + mask_card


def get_date(date: Union[str]) -> Union[str]:
    """
    функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024").
    """

    if not isinstance(date, str):
        raise TypeError("Не правильный тип даты")
    if len(str(date)) < 1:
        raise ValueError("Не правильный формат даты")
    filter_date = str(date)[:10].split("-")
    reversed_filter_date = filter_date[::-1]
    str_reversed_filter_date = str(
        reversed_filter_date[0] + "." + reversed_filter_date[1] + "." + reversed_filter_date[2]
    )
    return str_reversed_filter_date
