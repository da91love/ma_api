import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from common.util.EconoIndicator import EconoIndicator
from common.util.Validation import Validation
from common.const.KEY_NAME import KEY_NAME
from common.const.COMM import PERIOD_UNIT
import pydash as _

def create_market_summary_data(period_data: list, period_unit: str):
    # Create an instance
    validation = Validation()

    # group by period
    period_data_by_group = _.group_by(period_data, lambda v: v[KEY_NAME['PERIOD']])

    # Check below 4 datas are available
    # Get market cap, revenue, operation income, net income
    # Ger psr, por, per
    # Get market value per company
    result = []
    for period in period_data_by_group:
        # Period Validation
        if not validation.validate_period(tg_period= period, period_unit= period_unit):
            continue

        sum_data = {
            'tg_cmp_nb': 0,
            KEY_NAME['MV']: 0,
            KEY_NAME['SALES']: 0,
            KEY_NAME['OP']: 0,
            KEY_NAME['NP_CTRL']: 0,
        }

        # Sum all data by period
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

        # Add period to sum_data
        sum_data[KEY_NAME['PERIOD']] = period

        # 해당 Period에 대상 모집단 Company가 100개 이상일 시에 한해 결과값으로 인정
        # 100개 이하일 시 데이터 부족으로 탈락
        if sum_data['tg_cmp_nb'] > 100:
            result.append(sum_data)

    # Create temp_result to create multiple data
    # 멀티플 데이터 계산 시, 회사수가 다른 문제가 발생하여 각 매출, 영업이익, 당기순이익을 회사수로 나눈 값을 멀티플 재료로 활용
    temp_result = []
    for data in result:
        temp_result.append({
            KEY_NAME['MV']: data[KEY_NAME['MV']] / data['tg_cmp_nb'],
            KEY_NAME['SALES']: data[KEY_NAME['SALES']] / data['tg_cmp_nb'],
            KEY_NAME['OP']: data[KEY_NAME['OP']] / data['tg_cmp_nb'],
            KEY_NAME['NP_CTRL']: data[KEY_NAME['NP_CTRL']] / data['tg_cmp_nb'],
            KEY_NAME['PERIOD']: data[KEY_NAME['PERIOD']]
        })

    for data in temp_result:
        tg_period = data[KEY_NAME['PERIOD']]
        tg_period_data_in_result = _.find(result, {KEY_NAME['PERIOD']: tg_period})

        PSR = None
        POR = None
        PER = None
        if period_unit == PERIOD_UNIT['YEAR']:
            PSR = EconoIndicator.get_mltp(data[KEY_NAME['MV']], data[KEY_NAME['SALES']])
            POR = EconoIndicator.get_mltp(data[KEY_NAME['MV']], data[KEY_NAME['OP']])
            PER = EconoIndicator.get_mltp(data[KEY_NAME['MV']], data[KEY_NAME['NP_CTRL']])

        elif period_unit == PERIOD_UNIT['QUARTER']:
            sales_by_4prd = EconoIndicator.get_4prd_sum(KEY_NAME['SALES'], tg_period, temp_result, False)
            op_by_4prd = EconoIndicator.get_4prd_sum(KEY_NAME['OP'], tg_period, temp_result, False)
            np_by_4prd = EconoIndicator.get_4prd_sum(KEY_NAME['NP_CTRL'], tg_period, temp_result, False)

            PSR = EconoIndicator.get_mltp(data[KEY_NAME['MV']], sales_by_4prd)
            POR = EconoIndicator.get_mltp(data[KEY_NAME['MV']], op_by_4prd)
            PER = EconoIndicator.get_mltp(data[KEY_NAME['MV']], np_by_4prd)

        tg_period_data_in_result[KEY_NAME['PSR']] = PSR
        tg_period_data_in_result[KEY_NAME['POR']] = POR
        tg_period_data_in_result[KEY_NAME['PER']] = PER

    return result