import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import pydash as _
from common.util.FsUtil import FsUtil
from common.util.create_market_summary_data import create_market_summary_data
from common.const.COMM import PERIOD_UNIT
from common.const.KEY_NAME import KEY_NAME, OTHER_KEY_NAME
from common.const.PATH import *

def create_market_summary_data_wrapper():
    # import all data
    y_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_SUMMARY_DATA)
    q_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_SUMMARY_DATA)
    M2 = FsUtil.open_csv_2_json_file(project_root + KO_M2_DATA)[0]
    GDP = FsUtil.open_csv_2_json_file(project_root + KO_GDP_MODIFIED_DATA)[0]

    # market summary data 생성
    y_entire_market_data: list = create_market_summary_data(y_summary_data, PERIOD_UNIT['YEAR'])
    q_entire_market_data: list = create_market_summary_data(q_summary_data, PERIOD_UNIT['QUARTER'])

    # M2 와 year 및 quarter data 통합
    for data in y_entire_market_data:
        tg_period = data[KEY_NAME['PERIOD']]
        tg_data = _.find(y_entire_market_data, {KEY_NAME['PERIOD']: tg_period})

        tg_data[OTHER_KEY_NAME['M2']] = M2.get(tg_period)

        # gdp는 전년도 데이터와 비교해야하기 때문에 tg_gdp_period 산출
        tg_gdp_period = str(int((tg_period.split('/'))[0]) - 1) + '/' + tg_period.split('/')[1]
        tg_data[OTHER_KEY_NAME['GDP']] = GDP.get(tg_gdp_period)

    for data in q_entire_market_data:
        tg_period = data[KEY_NAME['PERIOD']]
        tg_data = _.find(q_entire_market_data, {KEY_NAME['PERIOD']: tg_period})

        tg_data[OTHER_KEY_NAME['M2']] = M2.get(tg_period)

        # gdp는 전년도 데이터와 비교해야하기 때문에 tg_gdp_period 산출
        tg_gdp_period = str(int((tg_period.split('/'))[0]) - 1) + '/' + tg_period.split('/')[1]
        tg_data[OTHER_KEY_NAME['GDP']] = GDP.get(tg_gdp_period)

    # save as csv
    FsUtil.save_json_2_csv_file(y_entire_market_data, project_root + KO_YEAR_MARKET_SUMMARY_DATA)
    FsUtil.save_json_2_csv_file(q_entire_market_data, project_root + KO_QUARTER_MARKET_SUMMARY_DATA)