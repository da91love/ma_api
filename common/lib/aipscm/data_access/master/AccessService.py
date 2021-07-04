from common.lib.aipscm.data_access.AccessServiceBase import AccessServiceBase
from common.lib.i18n.i18n import I18n
from .Query import Query


class AccessService(AccessServiceBase):

    @staticmethod
    @I18n([
        {'table_name': 'm_item_i18n', 'key_name': 'item_key'},
        {'table_name': 'm_item_group_i18n', 'key_name': 'item_group_cd'},
    ])
    def get_item(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_item, is_column=True, bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def get_snapshots(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_snapshots, is_column=True, bindings=bindings)

        except Exception as e:
            raise e
