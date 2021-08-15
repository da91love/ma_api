from common.lib.ma.data_access.system.AccessService import AccessService

def get_authed_user_id(auth_id: str):

    # Check user_id and pw
    lRes_auth_user_id = AccessService.select_auth_id(
        auth_id=auth_id
    )

    user_id = None
    for row in lRes_auth_user_id:
        if row['auth_id'] == auth_id:
            user_id = row['user_id']
            break

    return user_id
