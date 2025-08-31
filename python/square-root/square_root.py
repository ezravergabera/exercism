def square_root(number):
    if number <= 1:
        return number
    
    x0 = number / 2

    x1 = (x0 + number / x0) / 2

    while (x1 < x0):
        x0 = x1
        x1 = (x0 + number / x0) / 2

    return x0

    