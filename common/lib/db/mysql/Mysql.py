import logging
from common.util.config_get import get_config
import mysql.connector

# Set config
config = get_config()

# call instancese
logger = logging.getLogger()


class Mysql:

    connInstance = None

    @classmethod
    def getConnInstance(cls):
        try:
            if cls.connInstance is None:
                cls.__setConnInstance()

            return cls.connInstance

        except Exception as e:
            raise e

    @classmethod
    def __setConnInstance(cls):
        try:
            logger.info('mysql starts')

            # Get configuration of DB
            pgConf = config['DB']['mysql']

            rds_host = pgConf['db_host']
            rds_database = pgConf['db_database']
            rds_port = pgConf['db_port']
            rds_password = pgConf['db_password']
            rds_user = pgConf['db_user']

            conn = mysql.connector.connect(
                host=rds_host,
                database=rds_database,
                port=rds_port,
                user=rds_user,
                password=rds_password,
            )

            logger.info('mysql ends')
            cls.connInstance = conn

        except Exception as e:
            raise e
