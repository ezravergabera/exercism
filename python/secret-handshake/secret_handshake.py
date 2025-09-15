def commands(binary_str):
    reverse = False
    cmds = []
    for index, bit in enumerate(binary_str):
        if index == 0 and bit == "1":
            reverse = True
        if index == 1 and bit == "1":
            cmds.insert(0, "jump")
        if index == 2 and bit == "1":
            cmds.insert(0, "close your eyes")
        if index == 3 and bit == "1":
            cmds.insert(0, "double blink")
        if index == 4 and bit == "1":
            cmds.insert(0, "wink")

    if reverse:
        return cmds[::-1]
    else:
        return cmds