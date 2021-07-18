from common.lib.ma.data_access.system.AccessService import AccessService

def check_auth(user_id: str, auth_id: str):

    # Check user_id and pw
    lRes_auth_user_id = AccessService.select_auth_id(
        user_id=user_id
    )

    is_authed = False
    for row in lRes_auth_user_id:
        if row['auth_id'] == auth_id:
            is_authed = True
            break

    return is_authed
