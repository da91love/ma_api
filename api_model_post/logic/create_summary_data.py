from common.const.KEY_NAME import *
from common.util.EconoIndicator import EconoIndicator
from pandas import DataFrame as df
from pandas import Series
import pydash as _

def create_summary_data(summary, pl, bs, cf):

    try:
        for share_code in summary:
            print(share_code)
            tg_sc_summary = summary[share_code]
            tg_sc_pl: df = pl[share_code]
            tg_sc_bs: df = bs[share_code]
            tg_sc_cf: df = cf[share_code]

            for tg_period_summary in tg_sc_summary:
                period: str = tg_period_summary[SUMMARY_KEY_NAME['period']]

                tg_period_pl = _.find(tg_sc_pl, {'period': period})
                tg_period_bs = _.find(tg_sc_bs, {'period': period})
                tg_period_cf = _.find(tg_sc_cf, {'period': period})

                # if target period bs pl cf does not exist, return None
                ev: float = EconoIndicator.get_ev(tg_period_summary, tg_period_bs) if tg_period_summary and tg_period_bs else None
                ebitda: float = EconoIndicator.get_ebitda(tg_period_pl, tg_period_cf) if tg_period_pl and tg_period_cf else None
                ev_ebitda: float = EconoIndicator.get_ev_ebitda(ev, ebitda)

                tg_period_summary[SUMMARY_KEY_NAME['ev']] = ev
                tg_period_summary[SUMMARY_KEY_NAME['ebitda']] = ebitda
                tg_period_summary[SUMMARY_KEY_NAME['ev/ebitda']] = ev_ebitda

        return summary
    except Exception as e:
        raise e
