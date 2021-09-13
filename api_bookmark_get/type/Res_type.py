from common.type.base_res_type import BaseResType

class ResType(BaseResType):
    def __init__(self, value: dict):
        super().__init__()

        self.set_payload({
            'value': value,
        })
