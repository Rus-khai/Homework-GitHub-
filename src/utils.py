import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transactions(file_path):
    """ функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    """
    logger.info('Программа financial_transactions начала работу')

    try:
        with open(file_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
            logger.info('Идет проверка на правильность тип данных')
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error('Ошибка: FileNotFoundError')
        return []
    logger.info('Программа financial_transactions завершила работу')


print(financial_transactions('data/operations.json'))
