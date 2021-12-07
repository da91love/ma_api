from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from common.type.Errors import AuthenticationException
from common.util.get_authed_user_id import get_authed_user_id
from .type.Res_type import ResType
from .const.PATH import *
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
    params = event.get('params')
    country = params.get('country')

    year_result = None
    quarter_result = None
    if country == 'ko':
        year_result = json.load(open(project_root+KO_YEAR_SUMMARY_DATA, encoding="'UTF8'"))
        quarter_result = json.load(open(project_root+KO_QUARTER_SUMMARY_DATA, encoding="'UTF8'"))
    elif country == 'us':
        year_result = json.load(open(project_root+US_YEAR_SUMMARY_DATA, encoding="'UTF8'"))
        quarter_result = json.load(open(project_root+US_QUARTER_SUMMARY_DATA, encoding="'UTF8'"))

    result = {
        'year_result': year_result,
        'quarter_result': quarter_result
    }

    return ResType(value=result).get_response()

