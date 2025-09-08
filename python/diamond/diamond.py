def rows(letter):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
        "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, 
        "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
    }

    canvas = []

    if letter == "A":
        return "A"

    for num in range(letters[letter], 0, -1):
        if alphabet[num-1] == letter:
            line = alphabet[num-1] + "·"*letters.get(alphabet[num-1]) + alphabet[num-1]
            canvas.append(line)
            continue

        if alphabet[num-1] == "A":
            new_num = (letters.get(letter) + 1)//2
            line = "·"*new_num + "A" + "·"*new_num
            canvas.insert(0, line)
            canvas.append(line)
            continue

        symbol = "·"*(letters.get(letter) - ((letters[letter] - letters.get(alphabet[num-1])) * 2))
        line = symbol + alphabet[num-1] + symbol + alphabet[num-1] + symbol
        canvas.insert(0, line)
        canvas.append(line)




    return "\n".join(canvas)

print(rows("A"), "For A \n")
print(rows("C"), "For C \n")
print(rows("E"), "For E \n")