def label(colors):
    color_coding = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]

    res = ""
    for index, color in enumerate(colors):
        if index == 2:
            num_of_zero = 10 ** color_coding.index(color)
            res = int(res) * num_of_zero

            if res // 10**9 >= 1:
                res = str(res//10**9) + " gigaohms"
            elif res // 10**6 >= 1:
                res = str(res//10**6) + " megaohms"
            elif res // 10**3 >= 1:
                res = str(res//10**3) + " kiloohms"
            else:
                res = str(res) + " ohms"
            break

        if color in color_coding:
            if index == 0 and color.lower() == "black":
                continue
            res += str(color_coding.index(color))

    return str(res)

print(label(["orange", "orange", "black"]))
print(label(["red", "black", "red"]))
print(label(["blue", "violet", "blue"]))
print(label(["white", "white", "white"]))