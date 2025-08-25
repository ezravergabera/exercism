def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    number = str(digits)
    total = 0
    
    for index, num in enumerate(number[-1::-1]):
        total += (int(num) * (input_base ** index))

    res = ""
    while True:
        res += str(total%output_base)
        total = total//output_base
        if total == 1:
            res += "1"
            break

    return res[-1::-1]

print(rebase(10, 42, 2))