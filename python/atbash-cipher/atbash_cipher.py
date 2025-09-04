atbash = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789", "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba123456789")

def encode(plain_text):
    cipher = ""

    for chr in plain_text:
        if chr.isalnum():
            cipher += chr

    cipher = cipher.translate(atbash)

    count = 0

    for index, chr in enumerate(cipher):
        if index % 5 == 0:
            cipher = cipher[:index+count] + " " + cipher[index+count:]
            count += 1

    return cipher.strip()

def decode(ciphered_text):
    decoded_text = ciphered_text.replace(" ", "")

    return decoded_text.translate(atbash).strip()