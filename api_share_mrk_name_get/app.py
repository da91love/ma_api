from common.util.config_get import get_config
from common.AppBase import AppBase
from common.util.FsUtil import FsUtil
from .type.Res_type import ResType
from common.const.LOCAL_PATH import *
from .logic.ShareSearchInHeaderFormatter import ShareSearchInHeaderFormatter

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

    share_info = None
    market_info = None
    if country == 'ko':
        share_info = FsUtil.open_csv_2_json_file(project_root+KO_SHARE_INFO_DATA)
        market_info = json.load(open(project_root+KO_MRK_INFO_DATA, encoding="'UTF8'"))

    elif country == 'us':
        share_info = FsUtil.open_csv_2_json_file(project_root+KO_SHARE_INFO_DATA)
        market_info = json.load(open(project_root+KO_MRK_INFO_DATA, encoding="'UTF8'"))

    result = ShareSearchInHeaderFormatter.create_share_into_search_fmt(share_info) + ShareSearchInHeaderFormatter.create_market_into_search_fmt(market_info)

    return ResType(value=result).get_response()

