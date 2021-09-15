import pandas as pd
from pandas import DataFrame as df
import pydash as _
from ..logic.cut_data_by_term import cut_data_by_term

class Model:

    def __init__(self):
        None

    @staticmethod
    def get_turnaround_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return:
        """

        tg_shares = []

        # Get filter
        term_fltr = filter.get('termFilter')
        profit_type_fltr = filter.get('profitTypeFilter')

        for i, value in enumerate(quarterDataByShare):
            tg_share_info: list = quarterDataByShare.get(value)

            real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get('period')))
            tg_prd = filter.get('periodFilter') or _.last(real_data).get('period')
            tg_prd_data = cut_data_by_term(tg_share_info, tg_prd, term_fltr)
            tg_prd_data_len = len(tg_prd_data)

            try:
                # tg_prd_data should not be null: 원바이오젠과 같이 2019년 데이터까지 밖에 없는 지정 기간 내의 데이터가 존재하지 않으므로 걸러냄
                if tg_prd_data_len > 0:
                    # Latest period should be (+)
                    if _.last(tg_prd_data).get(profit_type_fltr) > 0:
                        # Past consecutive periods should be (-)
                        if _.every(_.slice_(tg_prd_data, 0, tg_prd_data_len - 1),
                                   lambda o: o.get(profit_type_fltr) < 0):
                            tg_shares.append(_.last(tg_prd_data))

            # dict.get(profit_type_fltr)의 값이 None과 같은 숫자가 아닐 경우, TypeError
            except TypeError as e:
                pass

        return tg_shares

    @staticmethod
    def get_value_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return:
        """
        None

    @staticmethod
    def get_bluechip_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return:
        """
        None

    @staticmethod
    def get_collapse_model(yearDataByShare: dict, filter: dict):
        """
        :param yearDataByShare: year data grouped by share
        :param filter: filter as object
        :return:
        """
        None

    @staticmethod
    def get_cp_growth_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return:
        """
        None

    @staticmethod
    def get_invst_growth_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return: 
        """
        None
