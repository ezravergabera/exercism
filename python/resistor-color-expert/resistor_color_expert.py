def resistor_label(colors):
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
    if len(colors) == 1 and colors[0] == "black":
        return '0 ohms'

    if len(colors) == 4:
        for index, color in enumerate(colors):
            if index == 3:
                if color == "grey":
                    res += " ±0.05%"
                if color == "violet":
                    res += " ±0.1%"
                if color == "blue":
                    res += " ±0.25%"
                if color == "green":
                    res += " ±0.5%"
                if color == "brown":
                    res += " ±1%"
                if color == "red":
                    res += " ±2%"
                if color == "gold":
                    res += " ±5%"
                if color == "silver":
                    res += " ±10%"
                break

            if index == 2:
                num_of_zero = 10 ** color_coding.index(color)
                res = int(res) * num_of_zero

                if res // 10**9 >= 1:
                    res = res/10**9
                    if str(res)[-1] == "0":
                        res = str(int(res))
                    res = str(res) + " gigaohms"
                elif res // 10**6 >= 1:
                    res = res/10**6
                    if str(res)[-1] == "0":
                        res = str(int(res))
                    res = str(res) + " megaohms"
                elif res // 10**3 >= 1:
                    res = res/10**3
                    if str(res)[-1] == "0":
                        res = str(int(res))
                    res = str(res) + " kiloohms"
                else:
                    res = str(res) + " ohms"
                continue

            if color in color_coding:
                if index == 0 and color.lower() == "black":
                    continue
                res += str(color_coding.index(color))

        return str(res)
    
    if len(colors) == 5:
        for index, color in enumerate(colors):
            if index == 4:
                if color == "grey":
                    res += " ±0.05%"
                if color == "violet":
                    res += " ±0.1%"
                if color == "blue":
                    res += " ±0.25%"
                if color == "green":
                    res += " ±0.5%"
                if color == "brown":
                    res += " ±1%"
                if color == "red":
                    res += " ±2%"
                if color == "gold":
                    res += " ±5%"
                if color == "silver":
                    res += " ±10%"
                break

            if index == 3:
                num_of_zero = 10 ** color_coding.index(color)
                res = int(res) * num_of_zero

                if res // 10**9 >= 1:
                    res = res/10**9
                    if str(res)[-1] == "0":
                        res = str(int(res))
                    res = str(res) + " gigaohms"
                elif res // 10**6 >= 1:
                    res = res/10**6
                    if str(res)[-1] == "0":
                        res = str(int(res))
                    res = str(res) + " megaohms"
                elif res // 10**3 >= 1:
                    res = res/10**3
                    if str(res)[-1] == "0":
                        res = str(int(res))
                    res = str(res) + " kiloohms"
                else:
                    res = str(res) + " ohms"
                continue

            if color in color_coding:
                if index == 0 and color.lower() == "black":
                    continue
                res += str(color_coding.index(color))

        return str(res)
    
print(resistor_label(["red", "black", "red", "green"]))