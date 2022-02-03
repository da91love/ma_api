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
            mv = summary.get(KEY_NAME['MV'])
            ibl = summary.get(KEY_NAME['I_B_LBLT'])
            cae = bs.get(KEY_NAME['CASH_N_EQVLT'])

            if NumUtil.is_digit(mv) and NumUtil.is_digit(ibl) and NumUtil.is_digit(cae):
                net_debt = ibl - cae
                ev = mv - net_debt
                return _.round_(ev, 2)
            else:
                return None

        except Exception:
            raise Exception


    @staticmethod
    def get_ebitda(pl, cf):
        try:
            oi = pl.get(KEY_NAME['OP'])
            onoie = pl.get(KEY_NAME['N_OP_INC_EXP'])
            dp = cf.get(KEY_NAME['DPRCT'])
            amz = cf.get(KEY_NAME['AMRTZ'])

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
    def get_ebitda_4prd_sum(tg_period, pl_period_results, cf_period_results):
        try:
            oi = EconoIndicator.get_4prd_sum(KEY_NAME['OP'], tg_period, pl_period_results)
            onoie = EconoIndicator.get_4prd_sum(KEY_NAME['N_OP_INC_EXP'], tg_period, pl_period_results)
            dp = EconoIndicator.get_4prd_sum(KEY_NAME['DPRCT'], tg_period, cf_period_results)
            amz = EconoIndicator.get_4prd_sum(KEY_NAME['AMRTZ'], tg_period, cf_period_results)

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
    def get_4prd_sum(idc: str, tg_period: str, period_results: list):
        try:
            # 타겟 기간의 인덱스를 찾음
            tg_prd_idx = _.sorted_index_by(period_results, {KEY_NAME['PERIOD']: tg_period}, KEY_NAME['PERIOD'])

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

    @staticmethod
    def get_margin(numerator, denominator):
        try:
            if NumUtil.is_digit(numerator) and NumUtil.is_digit(denominator):
                return _.round_((numerator/denominator) * 100, 2)
            else:
                return None

        # 당기순이익, 영업현금흐름 등이 0일때 ZeroDivisionError발생하므로 1로 인정
        except ZeroDivisionError:
            return _.round_((numerator / 1) * 100, 2)

        except Exception:
            raise Exception

    @staticmethod
    def get_mltp(mv: float, value: int):
        try:
            if NumUtil.is_digit(mv) and NumUtil.is_digit(value):
                return _.round_(mv/value, 2)
            else:
                return None

        # 당기순이익, 영업현금흐름 등이 0일때 ZeroDivisionError발생하므로 1로 인정
        except ZeroDivisionError:
            return _.round_(mv / 1, 2)

        except Exception:
            raise Exception

    @staticmethod
    def get_profit_per_share(numerator, denominator):
        try:
            if NumUtil.is_digit(numerator) and NumUtil.is_digit(denominator):
                return _.round_(numerator / denominator, 2)
            else:
                return None

        # 당기순이익, 영업현금흐름 등이 0일때 ZeroDivisionError발생하므로 1로 인정
        except ZeroDivisionError:
            return _.round_(numerator / 1, 2)

        except Exception:
            raise Exception