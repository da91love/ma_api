from common.util.config_get import get_config
import logging.config

# Create instance
config = get_config()
logging.config.dictConfig(config['LOG_CONFIG'])


def get_logger():

    logger = logging.getLogger()

    return logger
