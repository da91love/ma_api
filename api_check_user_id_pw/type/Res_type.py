from common.type.base_res_type import BaseResType

class ResType(BaseResType):
    def __init__(self, isIdNPwTrue: bool):
        super().__init__()

        self.set_payload({
            'isIdNPwTrue': isIdNPwTrue,
        })
