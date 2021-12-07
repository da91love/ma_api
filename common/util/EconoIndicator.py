import pydash as _
from pandas import DataFrame as df
from pandas import Series

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
    def get_ev(summary: Series, bs: df):
        try:
            mv = summary.loc[SUMMARY_KEY_NAME['mv']]
            ibl = summary.loc[SUMMARY_KEY_NAME['interestBearingLiabilities']]
            cae = bs.iloc[0][BS_KEY_NAME['cashAndEquivalents']]

            if NumUtil.is_digit(mv) and NumUtil.is_digit(ibl) and NumUtil.is_digit(cae):
                net_debt = ibl - cae
                ev = mv - net_debt
                return _.round_(ev, 2)
            else:
                return None

        except Exception:
            raise Exception


    @staticmethod
    def get_ebitda(pl: df, cf: df):
        try:
            oi = pl.iloc[0][PL_KEY_NAME['operationIncome']]
            onoie = pl.iloc[0][PL_KEY_NAME['otherNonOperationIncExp']]
            dp = cf.iloc[0][CF_KEY_NAME['depreciation']]
            amz = cf.iloc[0][CF_KEY_NAME['amortization']]

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

        except Exception:
            raise Exception