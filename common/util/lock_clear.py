import logging
from common.util.config_get import get_config
from common.lib.aipscm.data_access.system.AccessService import AccessService

# Set config
config = get_config()

# Create instancese
logger = logging.getLogger()


def clear_locks(lock_id):
    """
    :param lock_id: (str)
    """
    try:
        logger.info('clearLocks starts')

        # Execute sql
        sql_results = AccessService.get_all_locks(lock_id)

        for sql_result in sql_results:
            # TODO : sql_result[...] has dependency on insert_lock.sql
            item_key = sql_result[0]
            location_key = sql_result[1]
            lock_id = sql_result[2]

            AccessService.set_lock_invalid(item_key, location_key, lock_id)

        logger.info('clearLocks ends')

    except Exception as e:
        raise e
