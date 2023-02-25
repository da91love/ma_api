import pydash as _
from common.util.config_get import get_config
from common.AppBase import AppBase
from common.const.LOCAL_PATH import *
from common.util.FsUtil import FsUtil
from .type.Res_type import ResType


# import boto3
import json
import datetime
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
sys.path.append(api_root)


print(sys.path)
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
    country: str = data.get('country')

    year_result = None
    quarter_result = None
    if country == 'ko':
        # Open market summary data
        year_result = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_MARKET_SUMMARY_DATA)
        quarter_result = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_MARKET_SUMMARY_DATA)

        # Open macro data
        mrkcap = FsUtil.open_csv_2_json_file(project_root + KO_ALL_MRK_CAP_DATA)
        gdp = FsUtil.open_csv_2_json_file(project_root + KO_GDP_DATA)
        m2 = FsUtil.open_csv_2_json_file(project_root + KO_M2_DATA)

        for date in mrkcap:
            date_time_obj = datetime.strptime(date, '%Y/%m/%d')

            tg_year = date_time_obj.year
            tg_month = date_time_obj.month

            if gdp.get(date) is None:
                tg_date = (datetime.datetime(tg_year, 12, 31)).strftime('%Y/%m/%d')
                gdp[date] = gdp.get(tg_date)

            if m2.get(date) is None:
                tg_date = (datetime.datetime(tg_year, tg_month, 31)).strftime('%Y/%m/%d')
                m2[date] = m2.get(tg_date)


    elif country == 'us':
        year_result = FsUtil.open_csv_2_json_file(project_root+KO_YEAR_ADDED_SUMMARY_DATA)
        quarter_result = FsUtil.open_csv_2_json_file(project_root+KO_QUARTER_ADDED_SUMMARY_DATA)

    result: dict = {
        'mrk_smr': {
            'year_result': year_result,
            'quarter_result': quarter_result
        },
        'macro': {
            'gdp': gdp,
            'm2': m2,
            'mrkcap': mrkcap
        }

    }

    return ResType(value=result).get_response()


