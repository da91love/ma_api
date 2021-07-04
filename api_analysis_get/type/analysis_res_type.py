from common.type.base_res_type import BaseResType


class AnalysisResType(BaseResType):
    def __init__(self, busidate: str, closing_day: str, data: list):
        super().__init__()

        self.set_payload({
            'busidate': busidate,
            'closing_day': closing_day,
            'data': data
        })
