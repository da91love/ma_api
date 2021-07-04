import json
import pandas as pd
import logging
from pandas import DataFrame as df

from common.type.EntitySum import EntitySum
from common.type.EntityFirst import EntityFirst
from common.util.logger_get import get_logger

# Create instances
logger = get_logger()


def create_added_total_site_inv(data: list):
    try:
        logger.info('create_added_total_site_inv :: start')

        df_origin: df = pd.read_json(json.dumps(data), orient='columns')

        sum_tg_list: list = [
            EntityFirst.TOTAL_SITE_INV.value,
            EntitySum.WAREHOUSE_DELIVERY.value,
        ]

        df_base: df = df_origin[df_origin['entity'].isin(sum_tg_list)]

        columns: list = ['item_key', 'location_key', 'entity']

        # indexコラムのDF抽出
        df_index: df = df_base[columns]
        df_week = df_base.drop(columns=columns)

        # 計算のため空欄に0を入れ
        df_week.replace('', 0, inplace=True)

        # 計算のためストリングをFloatに変更
        df_week: df = df_week.astype(float)

        df_week.loc['total', :] = df_week.sum(axis=0)
        df_total: df = df_week.loc[["total"]]

        # item, location名取得
        item_key: str = df_index['item_key'].values[0]
        location_key: str = df_index['location_key'].values[0]

        # initialize list of lists
        data = [[item_key, location_key, 'ADDED_TOTAL_SITE_INV']]

        # Create the pandas DataFrame
        df_total_index: df = pd.DataFrame(
            data, columns=columns, index=['total'])

        df_row: df = pd.concat([df_total_index, df_total], axis=1)
        df_result: df = pd.concat([df_origin, df_row], axis=0)

        # Jsonに変化
        values: dict = json.loads(
            df_result.to_json(
                orient='index',
                date_format='iso'))
        result: list = [value for key, value in values.items()]

        logger.info('create_added_total_site_inv :: end')
        return result

    except Exception as e:
        raise e
