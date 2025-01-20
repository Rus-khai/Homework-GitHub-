from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> Union[str, int]:
    """
    Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    """
    str_card_number = str(card_number)
    return str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[-4:]


def get_mask_account(account_number: Union[str, int]) -> Union[str, int]:
    """
    Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    """
    str_account_number = str(account_number)
    return "**" + str_account_number[-4:]
