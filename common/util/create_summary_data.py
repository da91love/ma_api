from common.const.KEY_NAME import *
from common.util.EconoIndicator import EconoIndicator
from common.util.NumUtil import NumUtil
import pydash as _

def create_summary_data(period_unit: str, summary: dict, pl: dict, bs: dict, cf: dict):

    try:
        for share_code in summary:
            print(share_code)
            tg_sc_summary = summary.get(share_code)
            tg_sc_pl = pl.get(share_code)
            tg_sc_bs = bs.get(share_code)
            tg_sc_cf = cf.get(share_code)

            for tg_period_summary in tg_sc_summary:
                period: str = tg_period_summary[KEY_NAME['PERIOD']]

                tg_period_pl = _.find(tg_sc_pl, {'period': period})
                tg_period_bs = _.find(tg_sc_bs, {'period': period})
                tg_period_cf = _.find(tg_sc_cf, {'period': period})

                # if target period bs pl cf does not exist, return None
                if period_unit == 'year':
                    ebitda: float = EconoIndicator.get_y_ebitda(tg_period_pl, tg_period_cf) if tg_period_pl and tg_period_cf else None
                    ev: float = EconoIndicator.get_ev(tg_period_summary, tg_period_bs) if tg_period_summary and tg_period_bs else None
                    ev_ebitda: float = EconoIndicator.get_mltp(ev, ebitda)
                    epm: float = EconoIndicator.get_margin(ebitda, tg_period_summary[KEY_NAME['SALES']])

                    pbr: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], tg_period_summary[KEY_NAME['EQT_CTRL']])
                    bps: float = EconoIndicator.get_profit_per_share(tg_period_summary[KEY_NAME['EQT_CTRL']], NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                    psr: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], tg_period_summary[KEY_NAME['SALES']])
                    sps: float = EconoIndicator.get_profit_per_share(tg_period_summary[KEY_NAME['SALES']], NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                    por: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], tg_period_summary[KEY_NAME['OP']])
                    ops: float = EconoIndicator.get_profit_per_share(tg_period_summary[KEY_NAME['OP']], NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                    per: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], tg_period_summary[KEY_NAME['NP_CTRL']])
                    eps: float = EconoIndicator.get_profit_per_share(tg_period_summary[KEY_NAME['NP_CTRL']], NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                if period_unit == 'quarter':
                    sales_by_4prd = EconoIndicator.get_4prd_sum(KEY_NAME['SALES'], period, tg_sc_summary)
                    op_by_4prd = EconoIndicator.get_4prd_sum(KEY_NAME['OP'], period, tg_sc_summary)
                    np_by_4prd = EconoIndicator.get_4prd_sum(KEY_NAME['NP_CTRL'], period, tg_sc_summary)
                    ebitda: float = EconoIndicator.get_q_ebitda(period, tg_sc_pl, tg_sc_cf) if tg_period_pl and tg_period_cf else None

                    ev: float = EconoIndicator.get_ev(tg_period_summary, tg_period_bs) if tg_period_summary and tg_period_bs else None
                    ev_ebitda: float = EconoIndicator.get_mltp(ev, ebitda)
                    epm: float = EconoIndicator.get_margin(ebitda, sales_by_4prd)

                    pbr: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], tg_period_summary[KEY_NAME['EQT_CTRL']])
                    bps: float = EconoIndicator.get_profit_per_share(tg_period_summary[KEY_NAME['EQT_CTRL']], NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                    psr: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], sales_by_4prd)
                    sps: float = EconoIndicator.get_profit_per_share(sales_by_4prd, NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                    por: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], op_by_4prd)
                    ops: float = EconoIndicator.get_profit_per_share(op_by_4prd, NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                    per: float = EconoIndicator.get_mltp(tg_period_summary[KEY_NAME['MV']], np_by_4prd)
                    eps: float = EconoIndicator.get_profit_per_share(np_by_4prd, NumUtil.convert_num_as_unit(tg_period_summary[KEY_NAME['SHARE_NUM']], '억'))

                tg_period_summary[KEY_NAME['EV']] = ev
                tg_period_summary[KEY_NAME['EBITDA']] = ebitda
                tg_period_summary[KEY_NAME['EV_EBITDA']] = ev_ebitda
                tg_period_summary[KEY_NAME['EPM']] = epm
                tg_period_summary[KEY_NAME['PBR']] = pbr
                tg_period_summary[KEY_NAME['BPS']] = bps
                tg_period_summary[KEY_NAME['PSR']] = psr
                tg_period_summary[KEY_NAME['SPS']] = sps
                tg_period_summary[KEY_NAME['POR']] = por
                tg_period_summary[KEY_NAME['OPS']] = ops
                tg_period_summary[KEY_NAME['PER']] = per
                tg_period_summary[KEY_NAME['EPS']] = eps

        return summary
    except Exception as e:
        raise e