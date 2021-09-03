from common.type.base_res_type import BaseResType

class ResType(BaseResType):
    def __init__(self, is_id_n_pw_true: bool, auth_id: str):
        super().__init__()

        self.set_payload({
            'isIdNPwTrue': is_id_n_pw_true,
            'authId': auth_id,
        })
