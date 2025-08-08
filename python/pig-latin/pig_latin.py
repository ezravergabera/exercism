def translate(text):
    words = text.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    msg = ""

    # Rule 1
    for word in words:
        if word[0] in vowels or (word[0:2] == 'xr') or (word[0:2] == 'yt'):
            msg = word + "ay"
            break

        # Rule 2
        if word[0] not in vowels:
            temp = ""
            count = 0
            for i in range(len(word)):
                if word[i] in vowels:
                    break
                # Rule 3
                if word[i] == "q":
                    if word[i+1] == "u":
                        temp += "qu"
                        count += 2
                        break

                if word[i] not in vowels:
                    # Rule 4
                    if word[i] == "y" and word[i] != word[0]:
                        break
                    temp += word[i]
                    count += 1
            msg += word[count:] + temp + "ay "

    return msg.strip()