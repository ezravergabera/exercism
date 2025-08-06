def is_armstrong_number(number):
    num = str(number)
    total = 0
    for i in num:
        total += (int(i)**len(num))

    return False if total != number else True

print(is_armstrong_number(150))