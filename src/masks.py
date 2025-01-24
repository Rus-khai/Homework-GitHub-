from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> Union[str, int]:
    """
    Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    """
    str_card_number = str(card_number)
    if len(str_card_number) > 16 or len(str_card_number) < 16 or len(str_card_number) == 0:
        raise ValueError("Не правильный номер карты")
    return str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[-4:]


def get_mask_account(account_number: Union[str, int]) -> Union[str, int]:
    """
    Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    """
    str_account_number = str(account_number)
    if len(str_account_number) > 20 or len(str_account_number) < 20 or len(str_account_number) == 0:
        raise ValueError("Не правильный номер карты")
    return "**" + str_account_number[-4:]


