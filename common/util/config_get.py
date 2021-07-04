import os
import importlib


def get_config():

    try:
        env = os.environ.get('ENV', None)
        if env == "test":
            config_module = importlib.import_module('config.test')
        elif env == "demo":
            config_module = importlib.import_module('config.demo')
        elif env == "dev":
            config_module = importlib.import_module('config.development')
        elif env == "stg":
            config_module = importlib.import_module('config.staging')
        elif env == "prod":
            config_module = importlib.import_module('config.production')

        config = config_module.config
        return config

    except Exception as e:
        raise e
