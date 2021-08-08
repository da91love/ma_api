from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from common.type.Errors import AuthenticationException
from common.util.check_auth import check_auth
from .type.Res_type import ResType
# import boto3
import csv
import json
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
    user_id = data['userId']
    auth_id = data['authId']
    value = json.dumps(data['value'],  ensure_ascii=False)

    # Check authentication
    is_authed = check_auth(user_id=user_id, auth_id=auth_id)
    if not is_authed: raise AuthenticationException

    # Insert valuation data
    AccessService.insert_valuation(user_id=user_id, value=value)

    # select valuation data
    lRes_valuation: list = AccessService.select_valuation(user_id=user_id)

    json_value: list = [] if len(lRes_valuation) < 0 else lRes_valuation[0]['value']
    dict_value: dict = json.loads(json_value)

    return ResType(value=dict_value).get_response()

