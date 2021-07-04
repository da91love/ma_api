from common.lib.aipscm.data_access.AccessServiceBase import AccessServiceBase
from common.lib.i18n.i18n import I18n
from common.type.Errors import WrongSessionException
from .Query import Query


class AccessService(AccessServiceBase):

    @staticmethod
    def set_entity(*bindings):
        """
        :param bindings: (tuple)
        :return: (list) sql query result
        """
        try:
            return AccessServiceBase.execute_sql(
                sql=Query.sql_insert_entity, bindings=bindings)

        except Exception as e:
            raise WrongSessionException
