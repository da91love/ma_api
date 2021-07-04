import pandas as pd
import math
from decimal import *
from src.lib.aipscm.optimizer.site_inv_optm.SiteSalesEstimateModel import SiteSalesEstimateModel
from src.lib.aipscm.optimizer.site_inv_optm.EstimateAdjustModel import EstimateAdjustModel

import unittest


class SiteSalesEstimateModelTest(unittest.TestCase):

    # 季節係数割り戻しなしのパターン
    def test_without_season_factor(self):

        df = pd.DataFrame()
        df['date'] = pd.date_range('2019/01/09', '2019/02/14')
        df['num'] = [10, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3,
                     1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10]

        sm = SiteSalesEstimateModel(
            '2019/02/14', '2018/02/06', 4, df, EstimateAdjustModel(2.0, -1.75))

        self.assertEqual(sm.mu, Decimal(str(19.25)))
        self.assertEqual(sm.delta, Decimal(str(7.14)))

    # 季節係数割り戻しありパターン
    def test_with_season_factor(self):

        df = pd.DataFrame()
        df['date'] = pd.date_range('2019/01/09', '2019/02/14')
        df['num'] = [10, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3,
                     1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10]
        # 季節係数割戻しあり
        df['season_factor'] = [100] + \
            list(map(lambda x: x / 10, range(1, 36))) + [100]

        sm = SiteSalesEstimateModel(
            '2019/02/14', '2018/02/06', 4, df, EstimateAdjustModel(2.0, -1.75))

        self.assertEqual(sm.mu, Decimal(str(15.75)))
        self.assertEqual(sm.delta, Decimal(str(9.14)))

    # 異常値補正
    def test_with_adjust(self):

        df = pd.DataFrame()
        df['date'] = pd.date_range('2019/01/09', '2019/02/14')
        df['num'] = [10, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3,
                     1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 100, 10]

        sm = SiteSalesEstimateModel(
            '2019/02/14', '2018/02/06', 4, df, EstimateAdjustModel(2.0, -1.75))

        self.assertEqual(sm.mu, Decimal(str(22.5)))
        self.assertEqual(sm.delta, Decimal(str(10.41)))

    # 異常値補正なし
    def test_without_adjust(self):

        df = pd.DataFrame()
        df['date'] = pd.date_range('2019/01/09', '2019/02/14')
        df['num'] = [10, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3,
                     1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 100, 10]

        sm = SiteSalesEstimateModel('2019/02/14', '2018/02/06', 4, df)

        self.assertEqual(sm.mu, Decimal(str(43.50)))
        self.assertEqual(sm.delta, Decimal(str(50.16)))


if __name__ == '__main__':
    unittest.main()
