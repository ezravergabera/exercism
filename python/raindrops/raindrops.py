def convert(number):
    msg = ""

    if number % 3 == 0:
        msg += "Pling"

    if number % 5 == 0:
        msg += "Plang"

    if number % 7 == 0:
        msg += "Plong"

    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        msg += str(number)

    return msg