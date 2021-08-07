import logging
from common.util.config_get import get_config
import mysql.connector

# Set config
config = get_config()

# call instancese
logger = logging.getLogger()

class Mysql:

    '''
    getConnInstance 은 하나의 db connection만을 생성하기 위해, 싱글톤으로 작성됨.
    하지만 하나의 connection에서 작업을 하다보니, 여러 에러가 수반되게 되어 매 sql마다 새로운 connection을 생성하는 방법으로 변경
    https://stackoverflow.com/questions/65169638/mysqlconnector-python-new-db-connection-for-each-query-vs-one-single-connect
    '''
    # connInstance = None
    # @classmethod
    # def getConnInstance(cls):
    #     try:
    #         if cls.connInstance is None:
    #             cls.__setConnInstance()
    #
    #         return cls.connInstance
    #
    #     except Exception as e:
    #         raise e

    @classmethod
    def getConnInstance(cls):
        try:
            logger.info('mysql connection starts')

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

            logger.info('mysql connection ends')

            return conn

        except Exception as e:
            raise e
