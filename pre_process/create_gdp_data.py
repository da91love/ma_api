import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import pydash as _
from common.util.FsUtil import FsUtil
from common.const.LOCAL_PATH import *

def create_gdp_data():
    try:
        # import all data
        GDP = FsUtil.open_csv_2_json_file(project_root + KO_GDP_DATA)[0]

        modified_GDP = {}
        for period, value in GDP.items():
            gdp_year = (period.split('/'))[0]
            for month in ['/03', '/06', '/09', '/12']:
                create_period = gdp_year + month
                modified_GDP[create_period] = value

        # save as csv
        FsUtil.save_json_2_csv_file([modified_GDP], project_root + KO_GDP_MODIFIED_DATA)

    except Exception as e:
        raise e