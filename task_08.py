def multiply_numbers(inputs=None):
    if not isinstance(inputs, str):
        inputs = str(inputs)
    product = 1
    flag = 0
    for char in inputs:
        if char.isdigit():
            product *= int(char)
            flag = 1
    if flag == 1:
        return product
    else:
        return None
