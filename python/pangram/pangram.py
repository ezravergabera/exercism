def is_pangram(sentence):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    seen = []

    for char in sentence:
        if char.upper() in alphabet and char.upper() not in seen:
            seen.append(char.upper())

    return True if len(seen) == 26 else False