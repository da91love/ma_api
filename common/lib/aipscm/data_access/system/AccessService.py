from common.lib.aipscm.data_access.AccessServiceBase import AccessServiceBase
from common.lib.i18n.i18n import I18n
from .Query import Query


class AccessService(AccessServiceBase):
    @staticmethod
    @I18n([{'table_name': 'm_item_i18n',
            'key_name': 'item_key'}
           ])
    def marketing_kpi(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.test,
                is_column=True,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def insert_entity(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_insert_entity,
                is_column=True,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def insert_item_simulation(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_insert_item_simulation,
                is_column=True,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def get_crt_simulation(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_crt_smlt, is_column=True, bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    @I18n([{'table_name': 'm_candidate_group_i18n',
            'key_name': 'candidate_group_cd'},
           {'table_name': 'm_item_i18n',
            'key_name': 'item_key'},
           {'table_name': 'm_model_i18n',
            'key_name': 'model_cd'},
           ])
    def get_simulation(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_simulation, is_column=True, bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def get_item_crt_smlt_analysis(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_item_crt_smlt_analysis,
                is_column=True,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def get_item_crt_mdl_analysis(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_item_crt_mdl_analysis,
                is_column=True,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def get_analysis(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_analysis, is_column=True, bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    @I18n([
        {'table_name': 'm_item_i18n', 'key_name': 'item_key'},
        {'table_name': 'm_model_i18n', 'key_name': 'model_cd'},
        {'table_name': 'm_kpi_group_i18n', 'key_name': 'kpi_group_cd'},
        {'table_name': 'm_kpi_i18n', 'key_name': 'kpi_cd'},
        {'table_name': 'm_kpi_variation_i18n', 'key_name': 'kpi_variation_cd'},
        {'table_name': 'm_item_group_i18n', 'key_name': 'item_group_cd'},
    ])
    def get_kpi(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_kpi, is_column=True, bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def get_busidate(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_busidate, is_column=True, bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    @I18n([
        {'table_name': 'm_entity_i18n', 'key_name': 'entity_cd'},
        {'table_name': 'm_candidate_group_i18n', 'key_name': 'candidate_group_cd'},
        {'table_name': 'm_entity_candidate_i18n', 'key_name': 'entity_candidate_cd'},
    ])
    def get_candidate_detail(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_candidate_detail,
                is_column=True,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def get_item_model_info(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_select_item_model_info,
                is_column=True,
                bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    def insert_item_model(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_insert_item_model, is_column=True, bindings=bindings)

        except Exception as e:
            raise e

    @staticmethod
    @I18n([{'table_name': 'm_item_i18n', 'key_name': 'item_key'}])
    def i18n_test(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_item_test, is_column=True, bindings=bindings)

        except Exception as e:
            raise e
