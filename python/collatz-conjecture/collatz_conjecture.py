def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    no_of_steps = 0
    num = number
    list_of_no = []
    while num != 1:
        if num%2 == 0:
            num = num/2
        else:
            num = (num * 3) + 1

        no_of_steps += 1
        
        if num in list_of_no:
            break
        else: 
            list_of_no.append(num)

    return no_of_steps