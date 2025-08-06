def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    if number != 1:
        prev_number = 1
        for i in range(1, number):
            curr_number = prev_number * 2
            prev_number = curr_number
        return curr_number
    else:
        return 1 


def total():
    total = 1
 
    for i in range(2, 65):
        total += square(i)

    return total