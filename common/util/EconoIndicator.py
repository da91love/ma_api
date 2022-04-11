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
    def get_roic(op: dict, bs: dict):
        """
        "roic = noplat/유무형자산+운전자본변동" 이지만, 여기선 심플하게 "roic = op/유무형자산"으로 구한다
        """
        try:
            # 유형자산의 경우 반드시 존재하야 하는 값이지만, 무형자산의 경우, 0일 때 네이버 재무제표에 None값으로 인식되어
            # 에러가 발생하므로 0으로 처리(유형자산이 존재하지 않으면 투자대상 기업이 아니므로 무시해도 좋음)
            tangible_asst = bs.get(KEY_NAME['TGB_ASST'])
            intangible_asst = bs.get(KEY_NAME['INTGB_ASST']) or 0

            if NumUtil.is_digit(op) and NumUtil.is_digit(tangible_asst) and NumUtil.is_digit(intangible_asst):
                sales_related_asst = tangible_asst + intangible_asst
                roic = (op / sales_related_asst) * 100
                return _.round_(roic, 2)
            else:
                return None

        except Exception:
            raise Exception


    @staticmethod
    def get_ebitda(pl, cf):
        try:
            # 영업이익의 경우 반드시 존재해야만 하는 값이지만 onoie, dp, amz의 경우 0일 때 네이버 재무제표에 None값으로 인식되므로 0으로 처리
            ebit = pl.get(KEY_NAME['OP'])
            dp = cf.get(KEY_NAME['DPRCT']) or 0
            amz = cf.get(KEY_NAME['AMRTZ']) or 0

            if NumUtil.is_digit(ebit) and NumUtil.is_digit(dp) and NumUtil.is_digit(amz):
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
            ebit = EconoIndicator.get_4prd_sum(KEY_NAME['OP'], tg_period, pl_period_results, False)
            dp = EconoIndicator.get_4prd_sum(KEY_NAME['DPRCT'], tg_period, cf_period_results, True)
            amz = EconoIndicator.get_4prd_sum(KEY_NAME['AMRTZ'], tg_period, cf_period_results, True)

            if NumUtil.is_digit(ebit) and NumUtil.is_digit(dp) and NumUtil.is_digit(amz):
                da = dp + amz

                ebitda = ebit + da
                return _.round_(ebitda, 2)
            else:
                return None

        except Exception:
            raise Exception

    @staticmethod
    def get_4prd_sum(idc: str, tg_period: str, period_results: list, isNoneValueAccepted: bool):
        '''
        @param idc:
        @param tg_period:
        @param period_results:
        @param isNoneValueAccepted: 매출 영업이익과 같은 값은 반드시 존재해야 하는 값이기 때문에 데이터상 존재하지 않으면
        None을 반환하도록 했지만, 무형감가상각과 같은 경우는 0일 경우 네이버 재무제표에 숫자가 존재하지 않기에 None데이터여도 0으로 처리하도록 함
        @return:
        '''
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

                    if not value and isNoneValueAccepted: value = 0

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