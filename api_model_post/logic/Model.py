import pandas as pd
from pandas import DataFrame as df
import pydash as _
from common.util.EconoIndicator import EconoIndicator
from ..logic.cut_data_by_term import cut_data_by_term
from ..const.FILTER import *
from common.const.KEY_NAME import *

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
        term_fltr = filter.get(TERM)
        profit_type_fltr = filter.get(PROFIT_TYPE)

        for i, value in enumerate(quarterDataByShare):
            tg_share_info: list = quarterDataByShare.get(value)

            real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get(KEY_NAME['PERIOD'])))
            tg_prd = filter.get(PERIOD) or _.last(real_data).get(KEY_NAME['PERIOD'])
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

            # dict.get()의 값이 None과 같은 숫자가 아닐 경우: TypeError
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
        tg_shares = []

        # Get filter
        per_min_fltr = filter.get(PER_MIN)
        per_max_fltr = filter.get(PER_MAX)
        roe_min_fltr = filter.get(ROE_MIN)

        for i, value in enumerate(quarterDataByShare):
            tg_share_info: list = quarterDataByShare.get(value)

            real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get(KEY_NAME['PERIOD'])))
            tg_prd = filter.get(PERIOD) or _.last(real_data).get(KEY_NAME['PERIOD'])
            tg_prd_data = cut_data_by_term(tg_share_info, tg_prd)
            tg_prd_data_len = len(tg_prd_data)

            try:
                if tg_prd_data_len > 0:
                    last_prd_data = _.last(tg_prd_data)
                    tg_per = last_prd_data.get(KEY_NAME['PER'])
                    tg_roe = last_prd_data.get(KEY_NAME['ROE'])

                    # 0 < PER < 10 and ROE > 15
                    if per_min_fltr < tg_per <= per_max_fltr:
                        if roe_min_fltr <= tg_roe:
                            tg_shares.append(last_prd_data)

            # dict.get()의 값이 None과 같은 숫자가 아닐 경우: TypeError
            except TypeError as e:
                pass

        return tg_shares


    @staticmethod
    def get_bluechip_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return:
        """
        tg_shares = []

        # Get filter
        sales_min_fltr = filter.get(SALES_MIN)
        per_min_fltr = filter.get(PER_MIN)
        per_max_fltr = filter.get(PER_MAX)
        roe_min_fltr = filter.get(ROE_MIN)

        for i, value in enumerate(quarterDataByShare):
            tg_share_info: list = quarterDataByShare.get(value)

            real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get(KEY_NAME['PERIOD'])))
            tg_prd = filter.get(PERIOD) or _.last(real_data).get(KEY_NAME['PERIOD'])
            tg_prd_data = cut_data_by_term(tg_share_info, tg_prd)
            tg_prd_data_len = len(tg_prd_data)

            try:
                if tg_prd_data_len > 0:
                    last_prd_data = _.last(tg_prd_data)
                    tg_sales = last_prd_data.get(KEY_NAME['SALES'])
                    tg_per = last_prd_data.get(KEY_NAME['PER'])
                    tg_roe = last_prd_data.get(KEY_NAME['ROE'])

                    # 0 < PER < 10 and ROE > 15
                    if sales_min_fltr < tg_sales:
                        if per_min_fltr < tg_per <= per_max_fltr:
                            if roe_min_fltr <= tg_roe:
                                tg_shares.append(last_prd_data)

            # dict.get()의 값이 None과 같은 숫자가 아닐 경우: TypeError
            except TypeError as e:
                pass

        return tg_shares

    @staticmethod
    def get_collapse_model(yearDataByShare: dict, filter: dict):
        """
        :param yearDataByShare: year data grouped by share
        :param filter: filter as object
        :return:
        """
        tg_shares = []

        # Get filter
        mv_times_fltr = filter.get(MV_TIMES)
        term_fltr = filter.get(TERM)

        for i, value in enumerate(yearDataByShare):
            tg_share_info: list = yearDataByShare.get(value)

            real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get(KEY_NAME['PERIOD'])))
            tg_prd = filter.get(PERIOD) or _.last(real_data).get(KEY_NAME['PERIOD'])
            tg_prd_data = cut_data_by_term(tg_share_info, tg_prd, term_fltr)
            tg_prd_data_len = len(tg_prd_data)

            try:
                if tg_prd_data_len > 0:
                    last_prd_data = _.last(tg_prd_data)
                    last_mv = tg_prd_data[0].get(KEY_NAME['MV'])
                    this_mv = last_prd_data.get(KEY_NAME['MV'])

                    # if latest marketvalue is smaller than past marketvalue
                    if _.is_number(last_mv) & _.is_number(this_mv):
                        if (EconoIndicator.get_growth_rate(last_mv, this_mv)) < mv_times_fltr:
                            tg_shares.append(last_prd_data)

            # dict.get()의 값이 None과 같은 숫자가 아닐 경우: TypeError
            except TypeError as e:
                pass

        return tg_shares

    @staticmethod
    def get_cp_growth_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return:
        """
        tg_shares = []

        # Get filter
        op_times_fltr = filter.get(OP_TIMES)
        term_fltr = filter.get(TERM)
        profit_type_fltr = filter.get(PROFIT_TYPE)

        for i, value in enumerate(quarterDataByShare):
            tg_share_info: list = quarterDataByShare.get(value)

            real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get(KEY_NAME['PERIOD'])))
            tg_prd = filter.get(PERIOD) or _.last(real_data).get(KEY_NAME['PERIOD'])
            tg_prd_data = cut_data_by_term(tg_share_info, tg_prd, term_fltr)
            tg_prd_data_len = len(tg_prd_data)

            try:
                if tg_prd_data_len > 0:
                    last_prd_data = _.last(tg_prd_data)
                    last_op = tg_prd_data[0].get(profit_type_fltr)
                    this_op = last_prd_data.get(profit_type_fltr)

                    # if latest marketvalue is smaller than past marketvalue
                    if _.is_number(last_op) & _.is_number(this_op):
                        if (EconoIndicator.get_growth_rate(last_op, this_op)) > op_times_fltr:
                            tg_shares.append(last_prd_data)

            # dict.get()의 값이 None과 같은 숫자가 아닐 경우: TypeError
            except TypeError as e:
                pass

        return tg_shares

    @staticmethod
    def get_invst_growth_model(quarterDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return: 
        """

        # 정확히는 자본적 지출로 비교해야하는데 자본적 지출을 구하기 위한 데이터가 없음
        # 자본적 지출 = 유동자산 - 유동부채 + 감가상각비

        # tg_shares = []
        #
        # # Get filter
        # op_times_fltr = filter.get(OP_TIMES)
        # term_fltr = filter.get(TERM)
        #
        # for i, value in enumerate(quarterDataByShare):
        #     tg_share_info: list = quarterDataByShare.get(value)
        #
        #     real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get(KEY_NAME['PERIOD'])))
        #     tg_prd = filter.get(PERIOD) or _.last(real_data).get(KEY_NAME['PERIOD'])
        #     tg_prd_data = cut_data_by_term(tg_share_info, tg_prd, term_fltr)
        #     tg_prd_data_len = len(tg_prd_data)
        #
        #     try:
        #         if tg_prd_data_len > 0:
        #             last_prd_data = _.last(tg_prd_data)
        #             last_op = tg_prd_data[0].get(KEY_NAME['OP'])
        #             this_op = last_prd_data.get(KEY_NAME['OP'])
        #
        #             # if latest marketvalue is smaller than past marketvalue
        #             if _.is_number(last_op) & _.is_number(this_op):
        #                 if (EconoIndicator.get_growth_rate(last_op, this_op)) > op_times_fltr:
        #                     tg_shares.append(last_prd_data)
        #
        #     # dict.get()의 값이 None과 같은 숫자가 아닐 경우: TypeError
        #     except TypeError as e:
        #         pass

        return tg_shares

    @staticmethod
    def get_all_shares(periodDataByShare: dict, filter: dict):
        """
        :param quarterDataByShare: quarter data grouped by share
        :param filter: filter as object
        :return:
        """
        tg_shares = []

        for i, value in enumerate(periodDataByShare):
            tg_share_info: list = periodDataByShare.get(value)

            real_data = _.filter_(tg_share_info, lambda v: not ('E' in v.get(KEY_NAME['PERIOD'])))
            last_prd_data = _.last(real_data)

            try:
                if last_prd_data:
                    tg_shares.append(last_prd_data)

            # dict.get()의 값이 None과 같은 숫자가 아닐 경우: TypeError
            except TypeError as e:
                pass

        return tg_shares