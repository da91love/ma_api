import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from common.util.FsUtil import FsUtil
from common.util.EconoIndicator import EconoIndicator
from common.util.Validation import Validation
from common.const.KEY_NAME import KEY_NAME
from common.const.COMM import PERIOD_UNIT
from common.const.PATH import *
import pydash as _

def create_entire_market_data_wrapper():
    # import all data
    y_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_SUMMARY_DATA)
    q_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_SUMMARY_DATA)

    create_entire_market_data(y_summary_data, PERIOD_UNIT['YEAR'])
    create_entire_market_data(q_summary_data, PERIOD_UNIT['QUARTER'])


def create_entire_market_data(period_data, period_unit):
    # group by period
    period_data_by_group = _.group_by(period_data, lambda v: v[KEY_NAME['PERIOD']])

    # Check below 4 datas are available
    # Get market cap, revenue, operation income, net income
    # Ger psr, por, per
    # Get market value per company

    result = []
    for period in period_data_by_group:
        # Period Validation
        if not Validation.validate_period(tg_period= period, period_unit= period_unit):
            continue

        sum_data = {
            'tg_cmp_nb': 0,
            KEY_NAME['MV']: 0,
            KEY_NAME['SALES']: 0,
            KEY_NAME['OP']: 0,
            KEY_NAME['NP_CTRL']: 0,
        }
        for s_data in period_data_by_group[period]:
            mv = s_data.get(KEY_NAME['MV'])
            sales = s_data.get(KEY_NAME['SALES'])
            op = s_data.get(KEY_NAME['OP'])
            np_ctrl = s_data.get(KEY_NAME['NP_CTRL'])

            if mv and sales and op and np_ctrl:
                sum_data[KEY_NAME['MV']] += mv
                sum_data[KEY_NAME['SALES']] += sales
                sum_data[KEY_NAME['OP']] += op
                sum_data[KEY_NAME['NP_CTRL']] += np_ctrl

                sum_data['tg_cmp_nb'] += 1

        # Get psr por per
        sum_data[KEY_NAME['PSR']] = EconoIndicator.get_mltp(sum_data[KEY_NAME['MV']], sum_data[KEY_NAME['SALES']])
        sum_data[KEY_NAME['POR']] = EconoIndicator.get_mltp(sum_data[KEY_NAME['MV']], sum_data[KEY_NAME['OP']])
        sum_data[KEY_NAME['PER']] = EconoIndicator.get_mltp(sum_data[KEY_NAME['MV']], sum_data[KEY_NAME['NP_CTRL']])

        sum_data[KEY_NAME['PERIOD']] = period

        # 해당 Period에 대상 모집단 Company가 100개 이상일 시
        if sum_data['tg_cmp_nb'] > 100:
            result.append(sum_data)

    return result

create_entire_market_data_wrapper()