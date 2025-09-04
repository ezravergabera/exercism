atbash = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba")

def encode(plain_text):
    for chr in plain_text:
        if not chr.isalpha():
            cipher = plain_text.replace(chr, "")

    cipher = cipher.translate(atbash)

    return cipher.translate(atbash)


def decode(ciphered_text):
    return ciphered_text.translate(atbash)


print(encode("Testing,1 2 3, testing."))
print(encode("x123 yes"))
print(decode("vcvix rhn"))


stringgg = "hello"

