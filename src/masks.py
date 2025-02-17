import logging
from typing import Any, Union

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int]) -> Any:
    """
    Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    """
    logger.info('Программа get_mask_card_number начала работу')
    logger.info('Идет проверка на правильность карты')
    if not isinstance(card_number, (str, int)):
        logger.error('Был введён не правильный номер карты')
        raise TypeError("Не правильный тип номера карты")
    if len(str(card_number)) > 16 or len(str(card_number)) < 16 or len(str(card_number)) == 0:
        logger.error('Был введён не правильное количество цифр номера карты')
        raise ValueError("Не правильный номер карты")
    logger.info('Программа get_mask_card_number проверила правильность ввода номера карты')
    return str(card_number)[:4] + " " + str(card_number)[4:6] + "**" + " " + "****" + " " + str(card_number)[-4:]


def get_mask_account(account_number: Union[str, int]) -> Union[str]:
    """
    Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    """
    logger.info('Программа get_mask_account начала работу')
    logger.info('Идет проверка на правильность карты')
    if not isinstance(account_number, (str, int)):
        logger.error('Был введён не правильный номер счёта')
        raise TypeError("Не правильный тип счёта")
    if len(str(account_number)) > 20 or len(str(account_number)) < 20 or len(str(account_number)) == 0:
        logger.error('Был введён не правильный номер счёта')
        raise ValueError("Не правильный номер счёта")
    logger.info('Программа get_mask_account проверила правильность ввода номера счёта')
    return "**" + str(account_number)[-4:]

get_mask_card_number(1234123412341234)