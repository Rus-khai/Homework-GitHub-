from functools import wraps
from time import perf_counter


def log(filename=None):
    """
    Декоратор log, автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)
    """

    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            try:
                result = func(*args, **kwargs)
                end = perf_counter()
                log_message = f"{func.__name__} started at {start} and finished at {end:} with result: {result}"
                if filename is not None:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} ok\n")
                else:
                    print(log_message)
            except Exception as e:
                log_message_1 = f"{func.__name__} error {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message_1 + "\n")
                else:
                    print(log_message_1)
                raise e
            return result

        return wrapper

    return inner


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция, принимает 2 числа, и возвращает их сумму"""
    return x + y


my_function(1, 2)
