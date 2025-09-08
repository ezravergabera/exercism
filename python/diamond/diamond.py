def rows(letter):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = {
        "A": 0, "B": 1, "C": 3, "D": 5, "E": 7, "F": 9, "G": 11, "H": 13, "I": 15, "J": 17,
        "K": 19, "L": 21, "M": 23, "N": 25, "O": 27, "P": 29, "Q": 31, "R": 33, "S": 35, "T": 37, 
        "U": 39, "V": 41, "W": 43, "X": 45, "Y": 47, "Z": 49
    }

    canvas = []

    if letter == "A":
        return ["A"]

    for num in range(alphabet.index(letter)+1, 0, -1):
        if alphabet[num-1] == letter:
            line = alphabet[num-1] + " "*numbers.get(alphabet[num-1]) + alphabet[num-1]
            canvas.append(line)
            continue

        if alphabet[num-1] == "A":
            new_num = (numbers.get(letter) + 1)//2
            line = " "*new_num + "A" + " "*new_num
            canvas.insert(0, line)
            canvas.append(line)
            continue

        outer_symbol = " "*((numbers[letter] - numbers[alphabet[num-1]])//2)
        inner_symbol = " "*numbers[alphabet[num-1]]
        line = outer_symbol + alphabet[num-1] + inner_symbol + alphabet[num-1] + outer_symbol
        canvas.insert(0, line)
        canvas.append(line)

    return canvas