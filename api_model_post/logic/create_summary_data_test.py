from common.const.KEY_NAME import *
from common.util.EconoIndicator import EconoIndicator
from pandas import DataFrame as df
from pandas import Series

def create_summary_data(summary: df, pl: df, bs, cf: df):

    try:
        share_codes = summary[SUMMARY_KEY_NAME['shareCode']].unique()

        for share_code in share_codes:
            print(share_code)
            tg_sc_summary: df = summary.loc[summary[SUMMARY_KEY_NAME['shareCode']] == share_code]
            tg_sc_pl: df = pl.loc[pl[SUMMARY_KEY_NAME['shareCode']] == share_code]
            tg_sc_bs: df = bs.loc[bs[SUMMARY_KEY_NAME['shareCode']] == share_code]
            tg_sc_cf: df = cf.loc[cf[SUMMARY_KEY_NAME['shareCode']] == share_code]

            for index, row in tg_sc_summary.iterrows():
                period: str = row[SUMMARY_KEY_NAME['period']]

                tg_period_pl: df = tg_sc_pl.loc[tg_sc_pl[SUMMARY_KEY_NAME['period']] == period]
                tg_period_bs: df = tg_sc_bs.loc[tg_sc_bs[SUMMARY_KEY_NAME['period']] == period]
                tg_period_cf: df = tg_sc_cf.loc[tg_sc_cf[SUMMARY_KEY_NAME['period']] == period]

                # if target period bs pl cf does not exist, return None
                ev: float = None if row.empty or tg_period_bs.empty else EconoIndicator.get_ev(row, tg_period_bs)
                ebitda: float = None if tg_period_pl.empty or tg_period_cf.empty else EconoIndicator.get_ebitda(tg_period_pl, tg_period_cf)
                ev_ebitda: float = EconoIndicator.get_ev_ebitda(ev, ebitda)

                tg_sc_summary.loc[tg_sc_summary['period'] == period, [SUMMARY_KEY_NAME['ev']]] = ev
                tg_sc_summary.loc[tg_sc_summary['period'] == period, [SUMMARY_KEY_NAME['ebitda']]] = ebitda
                tg_sc_summary.loc[tg_sc_summary['period'] == period, [SUMMARY_KEY_NAME['ev/ebitda']]] = ev_ebitda

        return summary
    except Exception as e:
        raise e
