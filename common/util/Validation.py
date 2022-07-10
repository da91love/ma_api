from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

from common.const.COMM import PERIOD_UNIT

class Validation:
    def __init__(self):
        self._current_date = datetime.now()
        # self._current_year: int = self._current_date.year
        # self._current_month: int = self._current_date.month

    def validate_period(self, tg_period, period_unit):
        validation = True
        tg_year: int = int(tg_period.split('/')[0])
        tg_month: int = int(re.sub('\D', '', tg_period.split('/')[1]))
        tg_date: datetime = datetime(year=tg_year, month=tg_month, day=1)

        if period_unit == PERIOD_UNIT['YEAR']:
            # 12월이 아닌 연데이터 제외
            if tg_month != 12:
                validation = False

            # Forward 데이터 중 최근 년도보다 이전 년도 데이터 제외
            if validation and ('E' in tg_period) and (tg_date < self._current_date - relativedelta(months=4)):
                validation = False

        if period_unit == PERIOD_UNIT['QUARTER']:
            # 3 6 9 12월이 아닌 연데이터 제외
            if tg_month not in [3, 6, 9, 12]:
                validation = False

            # Forward 데이터 중 최근 분기보다 이전 분기 데이터 제외: ex) 2020/06(E)
            if validation and ('E' in tg_period) and (tg_date < self._current_date - relativedelta(months=4)):
                validation = False

        return validation