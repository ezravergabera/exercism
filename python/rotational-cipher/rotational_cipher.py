def rotate(text, key):
    # Time: O(n)
    rot_text = ""
    for char in text:
        if not char.isalpha():
            rot_text = rot_text + char
            continue
        if char.islower() and char.isalpha():
            rot_char = chr((((ord(char) - 97) + int(key)) % 26) + 97)
            rot_text = rot_text + rot_char
        if char.isupper() and char.isalpha():
            rot_char = chr((((ord(char) - 65) + int(key)) % 26) + 65)
            rot_text = rot_text + rot_char

    return rot_text