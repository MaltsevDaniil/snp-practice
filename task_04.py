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


print(sort_list([]))  # => []
print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
print(sort_list([1]))  # => [1, 1]
print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
