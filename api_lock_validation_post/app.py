from common.AppBase import AppBase
from common.util.lock_setting import set_locks
from common.util.lock_check import RLocksOn
from common.type.Errors import DataLockException
from common.type.Res import Res_frmt
import uuid
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
sys.path.append(api_root)


@AppBase
def lambda_handler(event, context=None) -> Res_frmt:
    """
    lambda_handler : This functions will be implemented in lambda
    :param event: (dict)
    :param context: (dict)
    :return: (dict)
    """
    # Get data from API Gateway
    data = event['body-json']['data']
    item = data['item_key']
    location = data['location_key']
    if not RLocksOn(item, location):
        # Create lockId
        lockId = str(uuid.uuid4())

        # Set lock
        set_locks(item, location, lockId)

        res = Res_frmt(lock=lockId).get_res()

        return res
    else:
        raise DataLockException
