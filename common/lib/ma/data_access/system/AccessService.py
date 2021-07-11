from common.lib.ma.data_access.AccessServiceBase import AccessServiceBase
# from common.lib.i18n.i18n import I18n
from .Query import Query


class AccessService(AccessServiceBase):

    @staticmethod
    def save_bookmark(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_save_bookmark,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def check_user_id_pw(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_check_user_id_pw,
                bindings=bindings)

        except Exception as e:
            raise e