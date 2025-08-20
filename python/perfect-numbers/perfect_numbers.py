def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = 0
    for x in range(1, number+1):
        if x == number:
            break
        if number % x == 0:
            aliquot_sum += x

    if aliquot_sum == number:
        res = "perfect"
    if aliquot_sum < number:
        res = "deficient"
    if aliquot_sum > number:
        res = "abundant"

    return res