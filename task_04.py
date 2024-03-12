def sort_list(list):
    res = []
    if len(list) != 0:
        maxi, mini = max(list), min(list)
        for i in range(len(list)):
            if list[i] == maxi:
                res.append(mini)
            elif list[i] == mini:
                res.append(maxi)
            else:
                res.append(list[i])
        res.append(mini)
    return res
