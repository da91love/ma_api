from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.aipscm.data_access.system.AccessService import AccessService
from common.util.total_site_inv_adder import create_added_total_site_inv
from common.util.day_to_week_converter import convert_day_to_week
from common.type.Errors import QueryParamInsufficientException
from .type.analysis_res_type import AnalysisResType
# import boto3
import csv
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
def lambda_handler(event, context=None) -> AnalysisResType:
    """
    lambda_handler : This functions will be implemented in lambda
    :param event: (dict)
    :param context: (dict)
    :return: (dict)
    """

    # Get data from API Gateway
    param = event['params']['querystring']
    simulation_key = param.get('simulation_key')

    analysisResType: list = ['test']

    return analysisResType.get_response()
