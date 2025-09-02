def is_paired(input_string):
    q = []

    for char in input_string:
        if char == "(" or char == "[" or char == "{":
            q.append(char)
            continue

        try:
            if char == ")" and q[-1] == "(":
                q.pop()
                continue

            if char == "]" and q[-1] == "[":
                q.pop()
                continue

            if char == "}" and q[-1] == "{":
                q.pop()
                continue

            if char == ")" or char == "]" or char == "}":
                q.append(char)
        except IndexError:
                return False
    
    return True if len(q) == 0 else False