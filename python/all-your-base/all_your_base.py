def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if any(d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    if any(d < 0 for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    total = 0
    for index, num in enumerate(digits):
        total += num * (input_base ** (len(digits)-1 - index))

    res = []
    while True:
        res.append(total%output_base)
        total = total//output_base
        if total == 1:
            res.append(1)
            break
        elif total == 0:
            break

    return res[-1::-1]