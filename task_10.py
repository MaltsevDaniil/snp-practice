import re
def count_words(string):
    res = {}
    string = string.lower()
    substring = re.sub(r'[^\w\s]', '', string)
    subarr = substring.split()
    for word in subarr:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res
print(count_words("A man, a plan, a canal -- Panama"))