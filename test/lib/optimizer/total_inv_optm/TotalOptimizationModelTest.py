import pandas as pd
import math
from decimal import *
from src.lib.aipscm.optimizer.total_inv_optm.TotalOptimizationModel import TotalOptimizationModel
import unittest


class TotalOptimizationModelTest(unittest.TestCase):
    def test_get_required_inv(self):
        demands = pd.DataFrame(
            [
                [
                    '20180101', 1562], [
                    '20180102', 1194], [
                    '20180103', 1027], [
                        '20180104', 1004], [
                            '20180105', 973], [
                                '20180106', 825], [
                                    '20180107', 974], [
                                        '20180108', 878], [
                                            '20180109', 1228], [
                                                '20180110', 1430], [
                                                    '20180111', 1458], [
                                                        '20180112', 1687], [
                                                            '20180113', 1454], [
                                                                '20180114', 1108], [
                                                                    '20180115', 1060]], columns=[
                                                                        'date', 'Num'])
        demands.date = pd.to_datetime(demands.date)
        arrivals = pd.DataFrame(
            [
                [
                    '20180101', 50], [
                    '20180102', 1250], [
                    '20180103', 500], [
                        '20180104', 6000], [
                            '20180105', 1300], [
                                '20180106', 2700], [
                                    '20180107', 1200], [
                                        '20180108', 800], [
                                            '20180109', 0], [
                                                '20180110', 0], [
                                                    '20180111', 0], [
                                                        '20180112', 0], [
                                                            '20180113', 0], [
                                                                '20180114', 0], [
                                                                    '20180115', 788]], columns=[
                                                                        'date', 'Num'])
        arrivals.date = pd.to_datetime(arrivals.date)

        model = TotalOptimizationModel(
            '20180101', 8, 1, 2, 0.36, 1.65, 20, demands, arrivals)
        self.assertEqual(model.required_inv_num, 16682)


if __name__ == '__main__':
    unittest.main()
