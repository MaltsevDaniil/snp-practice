def combine_anagrams(words_array):
    mp = {}
    for s in words_array:
        f = str(sorted(s))
        if f not in mp:
            mp[f] = []
        mp[f].append(s)
    return list(mp.values())
