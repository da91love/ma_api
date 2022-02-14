import pydash as _
from common.util.config_get import get_config
from common.AppBase import AppBase
from common.const.PATH import *
from common.util.FsUtil import FsUtil
from .type.Res_type import ResType
from .const.FS_FORMAT import FS_FMT
from .const.PATH_BY_STATUS import FS_PATH_KO

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


    if country == 'ko':
        for status in FS_PATH_KO:
            for period in FS_PATH_KO[status]:
                tg_path = FS_PATH_KO[status][period]
                tg_data = FsUtil.open_csv_2_json_file(project_root + tg_path)

                if share_code:
                    tg_data = _.filter_(tg_data, {'shareCode': share_code})

                FS_FMT[status][period] = tg_data

        # market_code is temporary stopped
        if market_code:
            None
            # year_result = (df_y_result.loc[df_y_result['marketCode'] == share_code]).to_dict('records')
            # quarter_result = (df_q_result.loc[df_q_result['marketCode'] == share_code]).to_dict('records')

    elif country == 'us':
        for status in FS_PATH_KO:
            for period in status:
                tg_path = FS_PATH_KO[status][period]
                tg_data = FsUtil.open_csv_2_json_file(project_root + tg_path)

                if share_code:
                    tg_data = _.filter_(tg_data, {'shareCode': share_code})

                FS_FMT[status][period] = tg_data

    return ResType(value=FS_FMT).get_response()


