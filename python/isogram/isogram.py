def is_isogram(string):
    letters = []
    for char in string:
        if char == " " or char == "-":
            continue

        if char.lower() in letters:
            return False
        letters.append(char.lower())
    return True