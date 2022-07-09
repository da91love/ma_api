from common.const.COMM import PERIOD_UNIT
import datetime

class Validation:
    @staticmethod
    def validate_period(tg_period, period_unit):
        validation = True
        tg_year = tg_period.split('/')[0]
        tg_month = tg_period.split('/')[1]

        current_date = datetime.datetime.now().date()
        current_year = current_date.strftime("%Y")
        current_month = current_date.strftime("%m")

        if period_unit == PERIOD_UNIT['YEAR']:
            if '12' not in tg_month:
                validation = False

            if validation and ('E' in tg_period) and (int(tg_year) < int(current_year)):
                validation = False

        return validation