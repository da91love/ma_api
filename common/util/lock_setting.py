import logging
from common.lib.db.postgre.Postgre import Postgre
from common.util.config_get import get_config
from common.lib.aipscm.data_access.system.AccessService import AccessService

# Set config
config = get_config()

# Create instancese
logger = logging.getLogger()

try:
    # Create DB connection
    conn = Postgre.getConnInstance()
except Exception as e:
    raise e


def set_locks(items, locs, lockId):
    """
    :param items: (list)
    :param locs: (list)
    :param lockId: (string)
    """
    logger.info('isLockOn starts')

    try:
        for item in items:
            for loc in locs:
                set_lock(item, loc, lockId)

        logger.info('RLocksOn ends')

    except Exception as e:
        logger.error(e)
        raise e


def set_lock(item, loc, lockId):
    """
    :param item: (string)
    :param loc: (string)
    :param lockId: (string)
    """
    logger.info('setLock starts')

    try:
        # Execute sql
        AccessService.set_lock(item, loc, lockId)
        logger.info('setLock ends')

    except Exception as e:
        logger.error(e)
        raise e
