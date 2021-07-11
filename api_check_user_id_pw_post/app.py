from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from .type.Res_type import ResType
# import boto3
import csv
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
    user_id = data['id']
    pw = data['pw']

    lRes_user_id_pw = AccessService.check_user_id_pw(
        user_id=user_id,
    )

    isIdNPwTrue = False
    for row in lRes_user_id_pw:
        if row['pw'] == pw:
            isIdNPwTrue = True
            break

    return ResType(isIdNPwTrue=isIdNPwTrue).get_response()
