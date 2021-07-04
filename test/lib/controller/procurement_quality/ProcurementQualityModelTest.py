import pandas as pd
import math
from decimal import *
from datetime import date
from src.lib.aipscm.common.datetime_util import datetime_util
from src.lib.aipscm.controller.procurement_quality.ProcurementQualityModel import ProcurementQualityModel
from src.lib.aipscm.controller.procurement_quality.ScaleAdjustModel import ScaleAdjustModel
from src.lib.aipscm.controller.procurement_quality.UnitAdjustModel import UnitAdjustModel
from src.lib.aipscm.optimizer.total_inv_optm.RequiredInvModel import RequiredInvModel

import unittest


class ProcurementQualityModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.demands = pd.DataFrame([['2018/01/01',
                                      1562],
                                     ['2018/01/02',
                                      1194],
                                     ['2018/01/03',
                                      1027],
                                     ['2018/01/04',
                                      1004],
                                     ['2018/01/05',
                                      973],
                                     ['2018/01/06',
                                      825],
                                     ['2018/01/07',
                                      974],
                                     ['2018/01/08',
                                      878],
                                     ['2018/01/09',
                                      1228],
                                     ['2018/01/10',
                                      1430],
                                     ['2018/01/11',
                                      1458],
                                     ['2018/01/12',
                                      1687],
                                     ['2018/01/13',
                                      1454],
                                     ['2018/01/14',
                                      1108],
                                     ['2018/01/15',
                                      1060],
                                     ['2018/01/16',
                                      1012],
                                     ['2018/01/17',
                                      989],
                                     ['2018/01/18',
                                      1536],
                                     ['2018/01/19',
                                      910],
                                     ['2018/01/20',
                                      913],
                                     ['2018/01/21',
                                      820],
                                     ['2018/01/22',
                                      656],
                                     ['2018/01/23',
                                      421],
                                     ['2018/01/24',
                                      332],
                                     ['2018/01/25',
                                      282],
                                     ['2018/01/26',
                                      227],
                                     ['2018/01/27',
                                      2],
                                     ['2018/01/28',
                                      2],
                                     ['2018/01/29',
                                      2],
                                     ['2018/01/30',
                                      2],
                                     ['2018/01/31',
                                      2],
                                     ['2018/02/01',
                                      2]],
                                    columns=['date',
                                             'Num'])
        self.demands.date = pd.to_datetime(self.demands.date)

        self.arrivals = pd.DataFrame([['2018/01/01',
                                       50],
                                      ['2018/01/02',
                                       1250],
                                      ['2018/01/03',
                                       500],
                                      ['2018/01/04',
                                       6000],
                                      ['2018/01/05',
                                       1300],
                                      ['2018/01/06',
                                       2700],
                                      ['2018/01/07',
                                       1200],
                                      ['2018/01/08',
                                       800],
                                      ['2018/01/09',
                                       0],
                                      ['2018/01/10',
                                       0],
                                      ['2018/01/11',
                                       0],
                                      ['2018/01/12',
                                       0],
                                      ['2018/01/13',
                                       0],
                                      ['2018/01/14',
                                       0],
                                      ['2018/01/15',
                                       788],
                                      ['2018/01/16',
                                       1132]],
                                     columns=['date',
                                              'Num'])
        self.arrivals.date = pd.to_datetime(self.arrivals.date)

        self.base_date = '2018/01/01'
        self.procurement_span = 2
        self.manufacture_lt = 15
        self.max_transfer_lt = 1
        self.target_date = datetime_util.add_day(datetime_util.to_date(
            self.base_date), int(self.manufacture_lt) + int(self.max_transfer_lt))

        self.demand_forecast_accuracy = 0.36
        self.safty_factor = 1.65
        self.min_inv = 20

        self.warehouse_inv_actual = 7137
        self.site_inv_actual = 1000

        self.scale_time_span = 6
        self.end_arrival_date = '2018/01/30'

        self.requiredinv_num = RequiredInvModel(
            self.base_date,
            self.target_date,
            self.procurement_span,
            self.demand_forecast_accuracy,
            self.safty_factor,
            self.min_inv,
            self.demands).requiredinv_num

    # 推奨調達数の確認
    def test_get_procurement_num(self):

        # get procurement num
        proc_model = ProcurementQualityModel(
            self.base_date,
            self.target_date,
            self.requiredinv_num,
            self.warehouse_inv_actual,
            self.site_inv_actual,
            self.arrivals,
            UnitAdjustModel(
                10,
                10000,
                1),
            ScaleAdjustModel(
                self.demands,
                self.scale_time_span,
                self.end_arrival_date))

        scale_adjusted = proc_model.procurement_num

        self.assertEqual(scale_adjusted, 1493 - 231)

    # 最小調達数の確認
    def test_get_procurement_num_min(self):

        # get procurement num
        proc_model = ProcurementQualityModel(
            self.base_date,
            self.target_date,
            self.requiredinv_num,
            self.warehouse_inv_actual,
            self.site_inv_actual,
            self.arrivals,
            UnitAdjustModel(
                5000,
                10000,
                1),
            ScaleAdjustModel(
                self.demands,
                self.scale_time_span,
                self.end_arrival_date))

        scale_adjusted = proc_model.procurement_num

        self.assertEqual(scale_adjusted, 5000)

    # 最大調達数の確認
    def test_get_procurement_num_max(self):

        # get procurement num
        proc_model = ProcurementQualityModel(
            self.base_date,
            self.target_date,
            self.requiredinv_num,
            self.warehouse_inv_actual,
            self.site_inv_actual,
            self.arrivals,
            UnitAdjustModel(
                1,
                20,
                1),
            ScaleAdjustModel(
                self.demands,
                self.scale_time_span,
                self.end_arrival_date))

        scale_adjusted = proc_model.procurement_num

        self.assertEqual(scale_adjusted, 20)

    # 調達単位の確認
    def test_get_procurement_num_unit(self):

        # get procurement num
        proc_model = ProcurementQualityModel(
            self.base_date,
            self.target_date,
            self.requiredinv_num,
            self.warehouse_inv_actual,
            self.site_inv_actual,
            self.arrivals,
            UnitAdjustModel(
                1,
                10000,
                3),
            ScaleAdjustModel(
                self.demands,
                self.scale_time_span,
                self.end_arrival_date))

        scale_adjusted = proc_model.procurement_num

        self.assertEqual(scale_adjusted, 1263)


if __name__ == '__main__':
    unittest.main()
