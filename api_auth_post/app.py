from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from .type.Res_type import ResType
# import boto3
import csv
import uuid
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
sys.path.append(api_root)

# Create instance
config = get_config()
# s3 = boto3.client(
#     's3',
#     aws_access_key_id=config['S3']['aws_access_key_id'],
#     aws_secret_access_key=config['S3']['aws_secret_access_key'],
# )

# get config data
s3_bucket_name = config['S3']['s3_bucket_name']


@AppBase
def lambda_handler(event, context=None) -> ResType:
    """
    lambda_handler : This functions will be implemented in lambda
    :param event: (dict)
    :param context: (dict)
    :return: (dict)
    """

    # Get data from API Gateway
    data = event['body-json']['data']
    user_id, pw = data.values()

    # Check user_id and pw
    lRes_user_id_pw = AccessService.select_user_id_pw(
        user_id=user_id,
    )

    is_id_n_pw_true = False
    for row in lRes_user_id_pw:
        if row['pw'] == pw:
            is_id_n_pw_true = True
            break

    # If user_id and pw is valid, register auth_id
    auth_id = None
    if is_id_n_pw_true:
        auth_id = str(uuid.uuid4())
        AccessService.insert_auth_id(
            user_id=user_id,
            auth_id=auth_id
        )

    return ResType(
                is_id_n_pw_true=is_id_n_pw_true,
                auth_id=auth_id
            ).get_response()
