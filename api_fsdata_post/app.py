from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from .type.Res_type import ResType
import pandas as pd
import numpy as np
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
    params = event.get('params')
    country = params.get('country')
    share_code = params.get('shareCode')
    market_code = params.get('marketCode')

    year_result = None
    quarter_result = None
    if country == 'ko':
        year_result_as_json = json.load(open(project_root+YEAR_RESULT_KO, encoding="'UTF8'"))
        quarter_result_as_json = json.load(open(project_root+QUARTER_RESULT_KO, encoding="'UTF8'"))

        df_y_result = pd.DataFrame.from_dict(year_result_as_json)
        df_q_result = pd.DataFrame.from_dict(quarter_result_as_json)

        if share_code:
            df_y_result_by_share = df_y_result.loc[df_y_result['shareCode'] == share_code]
            df_q_result_by_share = df_q_result.loc[df_q_result['shareCode'] == share_code]

            df_y_result_by_share = df_y_result_by_share.replace([np.nan], [None])
            df_q_result_by_share = df_q_result_by_share.replace([np.nan], [None])

            year_result: dict = df_y_result_by_share.to_dict('records')
            quarter_result: dict = df_q_result_by_share.to_dict('records')

        # market_code is temporary stopped
        if market_code:
            year_result = (df_y_result.loc[df_y_result['marketCode'] == share_code]).to_dict('records')
            quarter_result = (df_q_result.loc[df_q_result['marketCode'] == share_code]).to_dict('records')

    elif country == 'us':
        year_result = json.load(open(api_root+YEAR_RESULT_US, encoding="'UTF8'"))
        quarter_result = json.load(open(api_root+QUARTER_RESULT_US, encoding="'UTF8'"))

    result: dict = {
        'year_result': json.loads(json.dumps(year_result)),
        'quarter_result': json.loads(json.dumps(quarter_result))
    }

    return ResType(value=result).get_response()


