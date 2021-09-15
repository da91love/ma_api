# import boto3
import json
import os
import sys
import pandas as pd
import pydash as _
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
sys.path.append(api_root)

from common.util.config_get import get_config
from common.AppBase import AppBase
from .type.Res_type import ResType
from .logic.Model import Model

from .const.MODEL import *
from .const.PATH import *

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
    model = data.get('model')
    filter = data.get('filter')

    # Get raw data
    year_result: list = []
    quarter_result: list = []
    if country == 'ko':
        year_result = json.load(open(project_root+YEAR_RESULT_KO, encoding="'UTF8'"))
        quarter_result = json.load(open(project_root+QUARTER_RESULT_KO, encoding="'UTF8'"))

    elif country == 'us':
        year_result = json.load(open(api_root+YEAR_RESULT_US, encoding="'UTF8'"))
        quarter_result = json.load(open(api_root+QUARTER_RESULT_US, encoding="'UTF8'"))

    # Set raw data into dataframe
    y_result_by_share = _.group_by(year_result, lambda v: v['shareCode'])
    q_result_by_share = _.group_by(quarter_result, lambda v: v['shareCode'])

    # Run a model
    result = None
    if model == VALUE:
        result = Model.get_value_model(q_result_by_share, filter)
    elif model == TURNAROUND:
        result = Model.get_turnaround_model(q_result_by_share, filter)
    elif model == CPGROWTH:
        result = Model.get_cp_growth_model(q_result_by_share, filter)
    elif model == COLLAPSE:
        result = Model.get_collapse_model(y_result_by_share, filter)
    elif model == BLUECHIP:
        result = Model.get_bluechip_model(q_result_by_share, filter)
    elif model == INVGROWTH:
        result = Model.get_invst_growth_model(q_result_by_share, filter)

    return ResType(value=result).get_response()


