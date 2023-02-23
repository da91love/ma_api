import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import datetime

# open modules
import pydash as _
import requests

from common.util.FsUtil import FsUtil
from common.const.LOCAL_PATH import *
from common.const.API_PATH import *

# set instance
dt = datetime.datetime
crt_dt = dt.now().strftime('%Y-%m-%d')

def get_mrkcap():

    result = []
    tg_data = dt(2010, 1, 1)
    i = 0

    while (tg_data.strftime('%Y-%m-%d')) != crt_dt:

        str_tg_date = tg_data.strftime('%Y%m%d')

        # request to API
        res = requests.get(
            KRX_OPEN_API_GET_KOSPI_MRK_CAP_URL,
            headers={
                "AUTH_KEY": "D437B6E30BCB46B2B2FF96F80C4CCAABE5B91CD0"
            },
            params={
                "basDd": str_tg_date
            })

        # Get res as josn
        json_res = res.json()

        # Error handling if res is empty
        value = None
        try:
            value = (json_res.get('OutBlock_1'))[0]
        except IndexError:
            value = {}

        # Set API value into format
        res_format = {
            "BAS_DD": str_tg_date,
            "IDX_CLSS": value.get('IDX_CLSS'),
            "IDX_NM": value.get('IDX_NM'),
            "ACC_TRDVOL": value.get('ACC_TRDVOL'),
            "ACC_TRDVAL": value.get('ACC_TRDVAL'),
            "MKTCAP": value.get('MKTCAP')
        }

        # Append to result
        result.append(res_format)

        # Print log
        print(str_tg_date + ' done')

        # Add +1 day
        tg_data += datetime.timedelta(days=i+1)


    # save as csv
    FsUtil.save_json_2_csv_file(result, project_root + KO_KOSPI_MRK_CAP_DATA)


get_mrkcap()