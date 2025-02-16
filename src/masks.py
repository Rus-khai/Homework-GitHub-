from typing import Union
import logging


logger = logging.getLogger('masks.py')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks_logs.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



def get_mask_card_number(
    card_number: Union[
        str,
        int,
    ]
) -> Union[str]:
    """
    Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    """
    logger.info(f'Идет процесс процесс проверки типа карты {card_number}')
    if not isinstance(card_number, (str, int)):
        logger.error(f'Произошла ошибка.{TypeError}')
        raise TypeError("Не правильный тип номера карты")
    if len(str(card_number)) > 16 or len(str(card_number)) < 16 or len(str(card_number)) == 0:
        logger.error(f'Произошла ошибка.{ValueError}')
        raise ValueError("Не правильный номер карты")
    logger.info(f'Идет процесс процесс маскировки карты {card_number}')
    return str(card_number)[:4] + " " + str(card_number)[4:6] + "**" + " " + "****" + " " + str(card_number)[-4:]


def get_mask_account(account_number: Union[str, int]) -> Union[str]:
    """
    Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    """
    logger.info(f'Идет процесс процесс проверки типа счёта {account_number}')
    if not isinstance(account_number, (str, int)):
        logger.error(f'Произошла ошибка.{TypeError}')
        raise TypeError("Не правильный тип счёта")
    if len(str(account_number)) > 20 or len(str(account_number)) < 20 or len(str(account_number)) == 0:
        logger.error(f'Произошла ошибка.{TypeError}')
        raise ValueError("Не правильный номер счёта")
    logger.info(f'Идет процесс процесс маскировки счёта {account_number}')
    return "**" + str(account_number)[-4:]

get_mask_card_number(1234123412341234)
get_mask_account(12341234123412341234)