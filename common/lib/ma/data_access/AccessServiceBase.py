from common.type.Errors import WrongParameterException
from common.lib.db.postgre.Postgre import Postgre
from common.lib.db.postgre.sql_execution import executeSql

# Create instance
conn = Postgre.getConnInstance()


class AccessServiceBase:

    @staticmethod
    def execute_sql(sql, is_column=None, bindings=None):
        """
        :param sql:
        :param bindings:
        :return:
        """
        try:
            return executeSql(
                conn,
                sql,
                is_column=is_column,
                bindings=bindings)

        except Exception as e:
            raise e
