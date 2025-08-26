def value(colors):
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
    for color in colors:
        if color.lower() in color_coding:
            if len(res) == 2:
                break
            for index, x in enumerate(color_coding):
                if color == x:
                    res += str(index)
        
    return int(res)

