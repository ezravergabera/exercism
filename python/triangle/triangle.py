def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    count = 0

    if a == b:
        count += 1
    if b == c:
        count += 1
    if c == a:
        count += 1

    if count == 3:
        return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    count = 0

    if a == b:
        count += 1
    if b == c:
        count += 1
    if c == a:
        count += 1

    if count >= 1:
        if (a + b) <= c:
            return False
        elif (b + c) <= a:
            return False
        elif (a + c) <= b:
            return False
        else:
            return True
    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    count = 0

    if a == b:
        count += 1
    if b == c:
        count += 1
    if c == a:
        count += 1

    if count == 0:
        if (a + b) <= c:
            return False
        elif (b + c) <= a:
            return False
        elif (a + c) <= b:
            return False
        else:
            return True
    return False