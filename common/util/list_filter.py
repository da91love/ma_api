def filter_list(target: list, **conditions):
    """
    filter_list function
    :param target(list): target must be list which has dict inside
    :param conditions:
    :return(list): the list filtered with condition
    """
    try:
        result = []
        for ele in target:
            condition_counter = 0
            for key, value in conditions.items():
                if ele[key] == value:
                    condition_counter += 1

            if condition_counter == len(conditions):
                result.append(ele)

        return result

    except Exception as e:
        raise e
