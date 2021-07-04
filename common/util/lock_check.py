import logging
import datetime as dt
from common.util.config_get import get_config
from common.lib.aipscm.data_access.system.AccessService import AccessService

# Set config
config = get_config()

# Create instancese
logger = logging.getLogger()


def RLocksOn(items, locs, lock_id=None):
    """
    :param items: (list)
    :param locs: (list)
    :return: (boolean)
    """
    logger.info('RLocksOn starts')

    try:
        for item in items:
            for loc in locs:
                if isLockOn(item, loc, lock_id):
                    return True
                else:
                    pass

        logger.info('RLocksOn ends')
        return False

    except Exception as e:
        raise e


def isLockOn(item, loc, lock_id):
    """
    :param item: (string)
    :param loc: (string)
    :param lock_id: (string)
    :return: boolean
    """
    try:
        logger.info('isLockOn starts')

        # create sql
        if lock_id:
            lock_result = AccessService.get_lock_time_with_lockid(
                item, loc, lock_id)
        else:
            lock_result = AccessService.get_lock_time(item, loc)

        if not lock_result or _isAftLmtMin(lock_result):
            logger.info('Is Not Locked')
            logger.info('isLockOn ends')
            return False
        else:
            logger.info('Is Locked')
            logger.info('isLockOn ends')
            return True

    except Exception as e:
        raise e


def _isAftLmtMin(lock_result):
    """
    :param lock_result: (list)
    :return: (boolean)
    """
    try:
        if lock_result:
            LOCK_TIME_LIMIT = config['LOCK_TIME_LIMIT']
            prstTime = dt.datetime.now(dt.timezone.utc)
            lockTime = lock_result[0][0]
            lmtMin = dt.timedelta(minutes=LOCK_TIME_LIMIT)

            return prstTime > (lockTime + lmtMin)

        else:
            return None

    except Exception as e:
        raise e
