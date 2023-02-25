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
        year_result: list = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_MARKET_SUMMARY_DATA)
        quarter_result: list = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_MARKET_SUMMARY_DATA)

        # Open macro data
        mrkcap: list = FsUtil.open_csv_2_json_file(project_root + KO_ALL_MRK_CAP_DATA)
        gdp: dict = FsUtil.open_csv_2_json_file(project_root + KO_GDP_DATA)[0]
        m2: dict = FsUtil.open_csv_2_json_file(project_root + KO_M2_DATA)[0]

        # gdp 및 m2와 동일한 데이터 포맷으로 변경하기 위해 period가 key로 된 dict로 변형
        mrkcap_obj: dict = {}
        for data in mrkcap:
            mrkcap_obj[data.get('BAS_DD')] = data

        for date in mrkcap_obj:
            date_time_obj = datetime.datetime.strptime(date, '%Y/%m/%d')

            tg_year = date_time_obj.year
            tg_month = date_time_obj.month

            if gdp.get(date) is None:
                tg_date = (datetime.datetime(tg_year, 12, 1)).strftime('%Y/%m')
                gdp[date] = gdp.get(tg_date)

            if m2.get(date) is None:
                tg_date = (datetime.datetime(tg_year, tg_month, 1)).strftime('%Y/%m')
                m2[date] = m2.get(tg_date)


    elif country == 'us':
        year_result = FsUtil.open_csv_2_json_file(project_root+KO_YEAR_ADDED_SUMMARY_DATA)
        quarter_result = FsUtil.open_csv_2_json_file(project_root+KO_QUARTER_ADDED_SUMMARY_DATA)

    # gdp와 m2는 억원 단위로 return되고, 시가총액은 원단위로 return
    result: dict = {
        'mrk_smr': {
            'year_result': year_result,
            'quarter_result': quarter_result
        },
        'macro': {
            'gdp': gdp,
            'm2': m2,
            'mrkcap': mrkcap_obj
        }

    }

    return ResType(value=result).get_response()


