from common.util.config_get import get_config
from common.AppBase import AppBase
from common.const.PATH import *
from .logic.create_summary_data import create_summary_data
from .type.Res_type import ResType
import pandas as pd
import numpy as np

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
    country = data.get('country')
    share_code = data.get('shareCode')
    market_code = data.get('marketCode')


    year_result = None
    quarter_result = None
    if country == 'ko':
        df_y_summary_data = pd.read_csv(project_root+KO_YEAR_SUMMARY_DATA, dtype={'shareCode': str, 'marketCode': str})
        df_q_summary_data = pd.read_csv(project_root+KO_QUARTER_SUMMARY_DATA, dtype={'shareCode': str, 'marketCode': str})

        df_y_pl_data = pd.read_csv(project_root+KO_YEAR_PL_DATA, dtype={'shareCode': str, 'marketCode': str})
        df_q_pl_data = pd.read_csv(project_root+KO_QUARTER_PL_DATA, dtype={'shareCode': str, 'marketCode': str})

        df_y_bs_data = pd.read_csv(project_root+KO_YEAR_BS_DATA, dtype={'shareCode': str, 'marketCode': str})
        df_q_bs_data = pd.read_csv(project_root+KO_QUARTER_BS_DATA, dtype={'shareCode': str, 'marketCode': str})

        df_y_cf_data = pd.read_csv(project_root+KO_YEAR_CF_DATA, dtype={'shareCode': str, 'marketCode': str})
        df_q_cf_data = pd.read_csv(project_root+KO_QUARTER_CF_DATA, dtype={'shareCode': str, 'marketCode': str})

        if share_code:
            df_y_summary_data_by_share = df_y_summary_data.loc[df_y_summary_data['shareCode'] == share_code]
            df_q_summary_data_by_share = df_q_summary_data.loc[df_q_summary_data['shareCode'] == share_code]

            df_y_pl_data_by_share = df_y_pl_data.loc[df_y_pl_data['shareCode'] == share_code]
            df_q_pl_data_by_share = df_q_pl_data.loc[df_q_pl_data['shareCode'] == share_code]

            df_y_bs_data_by_share = df_y_bs_data.loc[df_y_bs_data['shareCode'] == share_code]
            df_q_bs_data_by_share = df_q_bs_data.loc[df_q_bs_data['shareCode'] == share_code]

            df_y_cf_data_by_share = df_y_cf_data.loc[df_y_cf_data['shareCode'] == share_code]
            df_q_cf_data_by_share = df_q_cf_data.loc[df_q_cf_data['shareCode'] == share_code]

            df_y_added_summary_data_by_share = create_summary_data(df_y_summary_data_by_share, df_y_pl_data_by_share, df_y_bs_data_by_share, df_y_cf_data_by_share)
            df_q_added_summary_data_by_share = create_summary_data(df_q_summary_data_by_share, df_q_pl_data_by_share, df_q_bs_data_by_share, df_q_cf_data_by_share)

            # df_y_result_by_share = df_y_result_by_share.where(df_y_result_by_share.notnull(), None)
            # df_q_result_by_share = df_q_result_by_share.where(df_q_result_by_share.notnull(), None)

            df_y_result_by_share = df_y_added_summary_data_by_share.replace([np.nan], [None])
            df_q_result_by_share = df_q_added_summary_data_by_share.replace([np.nan], [None])

            year_result: dict = df_y_result_by_share.to_dict('records')
            quarter_result: dict = df_q_result_by_share.to_dict('records')

        # market_code is temporary stopped
        if market_code:
            None
            # year_result = (df_y_result.loc[df_y_result['marketCode'] == share_code]).to_dict('records')
            # quarter_result = (df_q_result.loc[df_q_result['marketCode'] == share_code]).to_dict('records')

    elif country == 'us':
        year_result = json.load(open(api_root+US_YEAR_SUMMARY_DATA, encoding="'UTF8'"))
        quarter_result = json.load(open(api_root+US_QUARTER_SUMMARY_DATA, encoding="'UTF8'"))

    result: dict = {
        'year_result': year_result,
        'quarter_result': quarter_result
    }
    return ResType(value=result).get_response()


