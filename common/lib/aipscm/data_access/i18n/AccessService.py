from common.lib.aipscm.data_access.AccessServiceBase import AccessServiceBase
from common.type.Errors import WrongSessionException
from .Query import Query


class AccessService(AccessServiceBase):

    @staticmethod
    def translate(**bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_translate, is_column=True, bindings=bindings)

        except Exception as e:
            raise e
