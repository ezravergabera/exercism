def response(hey_bob):
    if len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"

    is_question = hey_bob.strip()[-1] == "?"
    is_capitalized = hey_bob.isupper()

    if is_question and is_capitalized:
        return "Calm down, I know what I'm doing!"
    
    if is_question:
        return "Sure."
    
    if is_capitalized:
        return "Whoa, chill out!"
    
    return "Whatever."
