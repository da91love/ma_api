import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import datetime
from functools import reduce
import copy

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
    all_mrkcap_e = FsUtil.open_csv_2_json_file(project_root + KO_ALL_MRK_CAP_DATA)

    # Set url
    api_url = (config.get('AUTH')).get('FRX_OPEN_API')

    # Get api data
    kospi_mrkcap_n = create_mrkcap_data(api_url, KRX_OPEN_API_GET_KOSPI_MRK_CAP_URL, kospi_mrkcap_e)
    kosdaq_mrkcap_n = create_mrkcap_data(api_url, KRX_OPEN_API_GET_KOSDAQ_MRK_CAP_URL, kosdaq_mrkcap_e)

    # Save as CSV
    FsUtil.save_json_2_csv_file(kospi_mrkcap_n, project_root + KO_KOSPI_MRK_CAP_DATA)
    FsUtil.save_json_2_csv_file(kosdaq_mrkcap_n, project_root + KO_KOSDAQ_MRK_CAP_DATA)

    # Sum
    grouped_mrkcap = _.group_by(kospi_mrkcap_n + kosdaq_mrkcap_n, lambda v: v['BAS_DD'])

    # # Set date checking list
    date_checking_list = []
    for d in all_mrkcap_e:
        date_checking_list.append(d.get('BAS_DD'))

    # Create mrkcap result as deepcopy
    all_mrkcap_n = copy.deepcopy(all_mrkcap_e)

    # Concating
    for date in grouped_mrkcap:
        if date in date_checking_list:
            pass
        else:
            tg_list: list = grouped_mrkcap.get(date)

            sumed_result = {}
            if tg_list[0].get('ACC_TRDVOL') is None:
                sumed_result = {
                    "BAS_DD": date,
                    "ACC_TRDVOL": None,
                    "ACC_TRDVAL": None,
                    "MKTCAP": None
                }
            else:
                acc_trdvol = reduce(lambda acc, cur: acc + cur["ACC_TRDVOL"], tg_list, 0)
                acc_trdval = reduce(lambda acc, cur: acc + cur["ACC_TRDVAL"], tg_list, 0)
                mktcap = reduce(lambda acc, cur: acc + cur["MKTCAP"], tg_list, 0)

                sumed_result = {
                    "BAS_DD": date,
                    "ACC_TRDVOL": acc_trdvol,
                    "ACC_TRDVAL": acc_trdval,
                    "MKTCAP": mktcap
                }

            all_mrkcap_n.append(sumed_result)

    # Save as CSV
    FsUtil.save_json_2_csv_file(all_mrkcap_n, project_root + KO_ALL_MRK_CAP_DATA)