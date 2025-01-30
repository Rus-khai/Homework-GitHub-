from typing import Union


def get_mask_card_number(card_number: Union[str, int,]) -> Union[str]:
    """
    Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    """

    if not isinstance(card_number, (str, int)):
        raise TypeError("Не правильный тип номера карты")
    if len(str(card_number)) > 16 or len(str(card_number)) < 16 or len(str(card_number)) == 0:
        raise ValueError("Не правильный номер карты")
    return str(card_number)[:4] + " " + str(card_number)[4:6] + "**" + " " + "****" + " " + str(card_number)[-4:]


def get_mask_account(account_number: Union[str, int]) -> Union[str]:
    """
    Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    """

    if not isinstance(account_number, (str, int)):
        raise TypeError("Не правильный тип счёта")
    if len(str(account_number)) > 20 or len(str(account_number)) < 20 or len(str(account_number)) == 0:
        raise ValueError("Не правильный номер счёта")
    return "**" + str(account_number)[-4:]
