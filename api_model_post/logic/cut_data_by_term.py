import pydash as _

def cut_data_by_term(tg_data, tg_prd, tg_term):
    """
    :param tg_data:
    :param tg_prd:
    :param tg_term:
    :return:
    """
    tg_prd_idx = _.find_index(tg_data, lambda v: v.get('period') == tg_prd)
    tg_data_to_tg_prd_idx = _.slice_(tg_data, 0, tg_prd_idx + 1)

    if tg_term:
        result: list = []
        for i in range(0, tg_term):
            lgth = len(tg_data_to_tg_prd_idx) - 1
            if lgth - 1 >= 0:
                _.unshift(result, tg_data_to_tg_prd_idx[lgth - i])
            else:
                break

        return result
    else :
        return tg_data_to_tg_prd_idx