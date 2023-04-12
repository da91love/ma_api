import datetime

from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from common.type.Errors import AuthenticationException
from common.const.API_PATH import *
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

# import module
import requests
import pydash as _

# Create instance
config = get_config()
now = datetime.datetime.now()
# s3 = boto3.client(
#     's3',
#     aws_access_key_id=config['S3']['aws_access_key_id'],
#     aws_secret_access_key=config['S3']['aws_secret_access_key'],
# )

# get config data
s3_bucket_name = config['S3']['s3_bucket_name']


@AppBase
def lambda_handler(event, context=None) -> ResType:

    # Get data from API Gateway
    header = event.get('header')
    auth_id = header.get('authId')
    service_item = (event.get('params')).get('shareCode')

    res = requests.get(NAVER_API_GET_STOCK_PRICE_URL, params={
        'query': f"SERVICE_ITEM:{service_item}"
    })

    json_res = res.json()
    datas: dict = ((json_res.get('result')).get('areas')[0]).get('datas')[0]

    return ResType(value=datas).get_response()

