import pydash as _
import math

class NumUtil:
    @staticmethod
    def is_digit(target):
        try:
            float(target)
            if math.isnan(target):
                raise Exception

            return True

        except Exception:
          return False

    @staticmethod
    def c_float_if_digit(target):
        try:
          c_float = float(target)
          return c_float
        except Exception:
          return target

    @staticmethod
    def divide_str(x, y):
        try:
          return _.round_(float(x)/float(y), 2)
        except Exception:
          return ""

    @staticmethod
    def convert_num_as_unit(num, unit):

        try:
            s = {
                "조": 1000000000000,
                "억": 100000000,
                "천만": 10000000,
                "백만": 1000000
            }

            if NumUtil.is_digit(num):
                return _.round_(num / s[unit], 2)
            else:
                return None

        except Exception:
            raise Exception


