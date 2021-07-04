import json
import pandas as pd
from pandas import DataFrame as df

from common.type.EntitySum import EntitySum
from common.type.EntityFirst import EntityFirst
from common.util.logger_get import get_logger

# Create instances
logger = get_logger()


def convert_day_to_week(data: list):
    try:
        logger.info("convert_day_to_week :: starts")

        df_flow: df = pd.read_json(json.dumps(data), orient='columns')

        result: list = []
        df_sum_targets: df = df_flow[df_flow['entity'].isin(
            [value for value, enum in EntitySum.__members__.items()])]
        sum_target_result: list = _sum_week_day_value(
            df_sum_targets, type='sum')
        result += sum_target_result

        df_first_targets: df = df_flow[df_flow['entity'].isin(
            [value for value, enum in EntityFirst.__members__.items()])]
        first_target_result: list = _sum_week_day_value(
            df_first_targets, type='first')
        result += first_target_result

        logger.info("convert_day_to_week :: ends")
        return result

    except Exception as e:
        raise e


def _sum_week_day_value(base_df: df, type: str):
    try:
        indexes: list = ['item_key', 'location_key', 'entity']

        # indexコラムのDF抽出
        df_index: df = base_df[indexes]
        df_week = base_df.drop(columns=indexes)

        # 計算のため空欄に0を入れ
        df_week.replace('', 0, inplace=True)

        # 計算のためストリングをFloatに変更
        df_flow = df_week.astype(float)

        # resample関数のため、コラムのデータタイプをdatetimeにCasting
        df_flow.columns = pd.to_datetime(df_flow.columns)

        if type == 'sum':
            df_filtered = df_flow.resample('W-MON', axis=1).sum()
        elif type == 'first':
            df_filtered = df_flow.resample('W-MON', axis=1).first()

        # Week名を持っているコラム名のString化
        df_filtered.columns = df_filtered.columns.strftime('%Y-%m-%d')

        # IndexDFとFilterの結果を結合
        df_result = pd.concat([df_index, df_filtered], axis=1)

        # Jsonに変化
        values: dict = json.loads(
            df_result.to_json(
                orient='index',
                date_format='iso'))
        result: list = [value for key, value in values.items()]

        return result

    except Exception as e:
        raise e