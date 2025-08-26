def color_code(color):
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

    if color.lower() in color_coding:
        for index, x in enumerate(color_coding):
            if color == x:
                return index
    
    raise ValueError("Color Not in list")


def colors():
    color = [
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
    return color