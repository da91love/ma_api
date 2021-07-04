from functools import wraps
from common.util.logger_get import get_logger
import time

logger = get_logger()


def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        process_time = time.time() - start
        logger.info(f"{func.__name__} takes {process_time} second")
        return result
    return wrapper
