import logging
from user_exceptions.ExceptionsForCreateHuman import InvalidIdError, InvalidNameError, InvalidAgeError


FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='log_file.log', filemode='a',
                    encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)


def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidNameError as e_name:
            logger.error(f'{e_name}')
        except InvalidAgeError as e_age:
            logger.error(f'{e_age}')
        except InvalidIdError as e_id:
            logger.error(f'{e_id}')
        return None
    return wrapper
