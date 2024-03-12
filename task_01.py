def is_palindrome(string):
    substing = "".join(i for i in str(string) if i.isalnum()).lower()
    return substing == substing[::-1]
