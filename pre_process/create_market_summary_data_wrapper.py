import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from common.util.FsUtil import FsUtil
from common.util.create_market_summary_data import create_market_summary_data
from common.const.COMM import PERIOD_UNIT
from common.const.PATH import *

def create_market_summary_data_wrapper():
    # import all data
    y_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_SUMMARY_DATA)
    q_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_SUMMARY_DATA)

    y_entire_market_data: list = create_market_summary_data(y_summary_data, PERIOD_UNIT['YEAR'])
    q_entire_market_data: list = create_market_summary_data(q_summary_data, PERIOD_UNIT['QUARTER'])

    # save as csv
    FsUtil.save_json_2_csv_file(y_entire_market_data, project_root + KO_YEAR_MARKET_SUMMARY_DATA)
    FsUtil.save_json_2_csv_file(q_entire_market_data, project_root + KO_QUARTER_MARKET_SUMMARY_DATA)