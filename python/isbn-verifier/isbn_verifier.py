def is_valid(isbn):
    sum = 0
    numbers = 10
    for digit in isbn:
        if digit.isalpha() and digit != "X" or digit == "X" and digit != isbn[-1]:
            return False

        if not digit.isnumeric() and digit !="X":
            continue

        if digit == "X":
            sum += 10 * numbers
        else:
            sum += int(digit) * numbers
        numbers -= 1

    # Time: O(n)

    return True if sum % 11 == 0 and numbers == 0 else False