import pydash as _
from common.util.config_get import get_config
from common.AppBase import AppBase
from common.const.PATH import *
from common.util.FsUtil import FsUtil
from .type.Res_type import ResType


# import boto3
import json
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
    share_code: list = data.get('shareCode')
    display_col: list = data.get('displayCol')
    market_code = data.get('marketCode')


    year_result = None
    quarter_result = None
    if country == 'ko':
        year_result = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_ADDED_SUMMARY_DATA, 'records')
        quarter_result = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_ADDED_SUMMARY_DATA, 'records')

        if share_code:
            year_result = _.filter_(year_result, lambda x: x['shareCode'] in share_code)
            quarter_result = _.filter_(quarter_result, lambda x: x['shareCode'] in share_code)

        if display_col:
            year_result_filtered_by_col = []
            for result_by_share in year_result:
                result_filtered_by_col = {}
                for col in display_col:
                    result_filtered_by_col[col] = result_by_share[col]
                year_result_filtered_by_col.append(result_filtered_by_col)
            year_result = year_result_filtered_by_col

            quarter_result_filtered_by_col = []
            for result_by_share in quarter_result:
                result_filtered_by_col = {}
                for col in display_col:
                    result_filtered_by_col[col] = result_by_share[col]
                quarter_result_filtered_by_col.append(result_filtered_by_col)
            quarter_result = quarter_result_filtered_by_col

        # market_code is temporary stopped
        if market_code:
            None
            # year_result = (df_y_result.loc[df_y_result['marketCode'] == share_code]).to_dict('records')
            # quarter_result = (df_q_result.loc[df_q_result['marketCode'] == share_code]).to_dict('records')

    elif country == 'us':
        year_result = FsUtil.open_csv_2_json_file(project_root+KO_YEAR_ADDED_SUMMARY_DATA, 'records')
        quarter_result = FsUtil.open_csv_2_json_file(project_root+KO_QUARTER_ADDED_SUMMARY_DATA, 'records')

    result: dict = {
        'year_result': year_result,
        'quarter_result': quarter_result
    }

    return ResType(value=result).get_response()


