def connect_dicts(dict1, dict2):
    sum_dict1 = sum(value for value in dict1.values())
    sum_dict2 = sum(value for value in dict2.values())
    if sum_dict1 > sum_dict2 or (sum_dict1 == sum_dict2 and len(dict1) > len(dict2)):
        priority_dict = dict1
        non_priority_dict = dict2
    else:
        priority_dict = dict2
        non_priority_dict = dict1

    final_dict = {}

    for key, value in priority_dict.items():
        if value >= 10:
            final_dict[key] = value

    for key, value in non_priority_dict.items():
        if value >= 10 and key not in final_dict:
            final_dict[key] = value

    return dict(sorted(final_dict.items(), key=lambda x: x[1]))
