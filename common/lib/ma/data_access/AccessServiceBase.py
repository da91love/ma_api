from common.type.Errors import WrongParameterException
from common.lib.db.mysql.Mysql import Mysql
from common.lib.db.mysql.sql_execution import executeSql

# Create instance
conn = Mysql.getConnInstance()

class AccessServiceBase:

    @staticmethod
    def execute_sql(sql, bindings=None):
        """
        :param sql:
        :param bindings:
        :return:
        """
        try:
            return executeSql(
                conn,
                sql,
                bindings=bindings)

        except Exception as e:
            raise e
