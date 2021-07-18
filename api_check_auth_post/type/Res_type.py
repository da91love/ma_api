from common.type.base_res_type import BaseResType

class ResType(BaseResType):
    def __init__(self, is_authed: bool):
        super().__init__()

        self.set_payload({
            'isAuthed': is_authed,
        })
