import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import datetime

# open modules
import pydash as _
import requests

from common.util.config_get import get_config
from common.util.FsUtil import FsUtil
from common.const.LOCAL_PATH import *
from common.const.API_PATH import *
from pre_process.create_mrkcap_data import create_mrkcap_data

# Create instance
config = get_config()
dt = datetime.datetime
crt_dt = dt.now().strftime('%Y-%m-%d')

def create_mrkcap_data_wrapper():

    # Open existing file
    kospi_mrkcap_e = FsUtil.open_csv_2_json_file(project_root + KO_KOSPI_MRK_CAP_DATA)
    kosdaq_mrkcap_e = FsUtil.open_csv_2_json_file(project_root + KO_KOSDAQ_MRK_CAP_DATA)

    # Set url
    api_url = (config.get('AUTH')).get('FRX_OPEN_API')

    # Get api data
    kospi_mrkcap_n = create_mrkcap_data(api_url, KRX_OPEN_API_GET_KOSPI_MRK_CAP_URL, kospi_mrkcap_e)
    kosdaq_mrkcap_n = create_mrkcap_data(api_url, KRX_OPEN_API_GET_KOSDAQ_MRK_CAP_URL, kosdaq_mrkcap_e)

    # Sum