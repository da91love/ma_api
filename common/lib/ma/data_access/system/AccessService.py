from common.lib.ma.data_access.AccessServiceBase import AccessServiceBase
# from common.lib.i18n.i18n import I18n
from .Query import Query


class AccessService(AccessServiceBase):

    """
    All function's name should start with below 4 verbs: select insert update delete
    """
    @staticmethod
    def select_bookmark(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_bookmark,
                bindings=bindings)

        except Exception as e:
            raise e



    @staticmethod
    def insert_bookmark(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_insert_bookmark,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def select_auth_id(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_auth_id,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def insert_auth_id(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_insert_auth_id,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def select_user_id_pw(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_user_id_pw,
                bindings=bindings)

        except Exception as e:
            raise e