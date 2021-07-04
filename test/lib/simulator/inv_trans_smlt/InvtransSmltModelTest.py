import pandas as pd
from src.lib.aipscm.simulator.inv_trans_smlt.InvTransSmltModel import InvTransSmltModel
import unittest


class InvTransSmltModelTest(unittest.TestCase):
    def test_inv_num_next(self):
        model = InvTransSmltModel(300, 120, 100)
        self.assertEqual(model.inv_num, 320)


if __name__ == '__main__':
    unittest.main()
