import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from common.util.create_summary_data import create_summary_data
from common.util.FsUtil import FsUtil
from common.const.PATH import *
import pydash as _

def create_summary_data_wrapper():
    y_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_SUMMARY_DATA, 'records')
    q_summary_data = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_SUMMARY_DATA, 'records')

    y_pl_data = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_PL_DATA, 'records')
    q_pl_data = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_PL_DATA, 'records')

    y_bs_data = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_BS_DATA, 'records')
    q_bs_data = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_BS_DATA, 'records')

    y_cf_data = FsUtil.open_csv_2_json_file(project_root + KO_YEAR_CF_DATA, 'records')
    q_cf_data = FsUtil.open_csv_2_json_file(project_root + KO_QUARTER_CF_DATA, 'records')

    # group by
    y_summary_data_by_share = _.group_by(y_summary_data, lambda v: v['shareCode'])
    q_summary_data_by_share = _.group_by(q_summary_data, lambda v: v['shareCode'])

    y_pl_data_by_share = _.group_by(y_pl_data, lambda v: v['shareCode'])
    q_pl_data_by_share = _.group_by(q_pl_data, lambda v: v['shareCode'])

    y_bs_data_by_share = _.group_by(y_bs_data, lambda v: v['shareCode'])
    q_bs_data_by_share = _.group_by(q_bs_data, lambda v: v['shareCode'])

    y_cf_data_by_share = _.group_by(y_cf_data, lambda v: v['shareCode'])
    q_cf_data_by_share = _.group_by(q_cf_data, lambda v: v['shareCode'])

    # Run create summary data
    y_added_summary_data = create_summary_data('year', y_summary_data_by_share, y_pl_data_by_share, y_bs_data_by_share, y_cf_data_by_share)
    q_added_summary_data = create_summary_data('quarter', q_summary_data_by_share, q_pl_data_by_share, q_bs_data_by_share, q_cf_data_by_share)

    # De-group
    y_degrouped_summary_data = _.flatten([y_added_summary_data[i] for i in y_added_summary_data])
    q_degrouped_summary_data = _.flatten([q_added_summary_data[i] for i in q_added_summary_data])

    # save as csv
    FsUtil.save_json_2_csv_file(y_degrouped_summary_data, project_root + KO_YEAR_ADDED_SUMMARY_DATA)
    FsUtil.save_json_2_csv_file(q_degrouped_summary_data, project_root + KO_QUARTER_ADDED_SUMMARY_DATA)
