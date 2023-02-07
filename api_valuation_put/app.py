from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from common.type.Errors import AuthenticationException
from common.util.get_authed_user_id import get_authed_user_id
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
    data = (event.get('body-json')).get('data')
    header = event.get('header')
    share_code = data.get('shareCode')

    auth_id = header.get('authId')
    # value = json.dumps(data.get('value'),  ensure_ascii=False)
    value = data.get('value')


    # Check authentication
    user_id = get_authed_user_id(auth_id=auth_id)
    if not user_id: raise AuthenticationException

    # select valuation data to update
    existing_value: list = AccessService.select_valuation(user_id=user_id)

    json_existing_value: list = [] if len(existing_value) < 0 else (existing_value[0]).get('value')
    dict_existing_value: dict = json.loads(json_existing_value)
    dict_existing_value[share_code] = value

    # dict 상태로 update후 db로 삽입 위해 json 화
    updated_json_existing_value = json.dumps(dict_existing_value,  ensure_ascii=False)

    # Insert valuation data
    AccessService.insert_valuation(user_id=user_id, value=updated_json_existing_value)

    return ResType(value=value).get_response()

