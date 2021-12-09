import pydash as _

from common.const.KEY_NAME import *
from common.util.NumUtil import NumUtil

class EconoIndicator:
    @staticmethod
    def get_growth_rate(last, this):
        """
        :param last:
        :param this:
        :return: The unit of return value is percentage
        """
        if last == 0:
            return (this-1/abs(1)) * 100
        else:
            return ((this - last)/abs(last)) * 100

    @staticmethod
    def get_ev(summary: dict, bs: dict):
        try:
            mv = summary.get(SUMMARY_KEY_NAME['mv'])
            ibl = summary.get(SUMMARY_KEY_NAME['interestBearingLiabilities'])
            cae = bs.get(BS_KEY_NAME['cashAndEquivalents'])

            if NumUtil.is_digit(mv) and NumUtil.is_digit(ibl) and NumUtil.is_digit(cae):
                net_debt = ibl - cae
                ev = mv - net_debt
                return _.round_(ev, 2)
            else:
                return None

        except Exception:
            raise Exception


    @staticmethod
    def get_y_ebitda(pl, cf):
        try:
            oi = pl.get(PL_KEY_NAME['operationIncome'])
            onoie = pl.get(PL_KEY_NAME['otherNonOperationIncExp'])
            dp = cf.get(CF_KEY_NAME['depreciation'])
            amz = cf.get(CF_KEY_NAME['amortization'])

            if NumUtil.is_digit(oi) and NumUtil.is_digit(onoie) and NumUtil.is_digit(dp) and NumUtil.is_digit(amz):
                ebit = oi + onoie
                da = dp + amz

                ebitda = ebit + da
                return _.round_(ebitda, 2)
            else:
                return None

        except Exception:
            raise Exception

    @staticmethod
    def get_q_ebitda(tg_period, pl_period_results, cf_period_results):
        try:
            oi = EconoIndicator.get_4prd_sum(PL_KEY_NAME['operationIncome'], tg_period, pl_period_results)
            onoie = EconoIndicator.get_4prd_sum(PL_KEY_NAME['otherNonOperationIncExp'], tg_period, pl_period_results)
            dp = EconoIndicator.get_4prd_sum(CF_KEY_NAME['depreciation'], tg_period, cf_period_results)
            amz = EconoIndicator.get_4prd_sum(CF_KEY_NAME['amortization'], tg_period, cf_period_results)

            if NumUtil.is_digit(oi) and NumUtil.is_digit(onoie) and NumUtil.is_digit(dp) and NumUtil.is_digit(amz):
                ebit = oi + onoie
                da = dp + amz

                ebitda = ebit + da
                return _.round_(ebitda, 2)
            else:
                return None

        except Exception:
            raise Exception

    @staticmethod
    def get_ev_ebitda(ev: float, ebitda: float):
        try:
            if NumUtil.is_digit(ev) and NumUtil.is_digit(ebitda):

                ev_ebitda = _.round_(ev/ebitda, 2)
                return ev_ebitda
            else:
                return None

        except ZeroDivisionError:
            return _.round_(ev / 0.1, 2)

        except Exception:
            raise Exception

    @staticmethod
    def get_4prd_sum(idc: str, tg_period: str, period_results: list):
        try:
            # 타겟 기간의 인덱스를 찾음
            tg_prd_idx = _.sorted_index_by(period_results, {SUMMARY_KEY_NAME['period']: tg_period}, SUMMARY_KEY_NAME['period'])

            sum = 0
            # 타겟 기간 포함 4연속 기간의 데이터가 존재하지 않을시 None값 리턴
            if tg_prd_idx < 3:
                return None
            else:
                for i in range(0, 4):
                    # 과거 4년치 데이터 중 데이터가 하나라도 없는 경우 None 반환
                    value = (period_results[tg_prd_idx - i]).get(idc)
                    if NumUtil.is_digit(value):
                        sum += value
                    else:
                        return None

            return sum

        except Exception as e:
            raise e