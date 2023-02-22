import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import datetime

# open modules
import pydash as _
import requests

# set instance
dt = datetime.datetime

def create_mrkcap_data(auth_key: str, api_url: str, mrkcap_date_e: list):

    # Set variables
    result = []
    tg_data = dt(2010, 1, 1)
    crt_dt = dt.now().strftime('%Y-%m-%d')
    i = 0

    # Set date checking list
    date_checking_list = []
    for d in mrkcap_date_e:
        date_checking_list.append(d.get('BAS_DD'))

    while (tg_data.strftime('%Y-%m-%d')) != crt_dt:

        # Set target date as str
        str_tg_date = tg_data.strftime('%Y%m%d')

        # 기존 데이터에서 존재하면 그냥 PASS
        if str_tg_date in date_checking_list:
            # Print log
            print(str_tg_date + ' done')

            # Add +1 day
            tg_data += datetime.timedelta(days=i+1)

        else:
            # request to API
            res = requests.get(
                api_url,
                headers={"AUTH_KEY": auth_key},
                params={"basDd": str_tg_date}
            )

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

    return result
