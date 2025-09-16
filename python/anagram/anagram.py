def find_anagrams(word, candidates):
    anagrams = []
    target = list(word.upper())
    target.sort()
    for candidate in candidates:
        candidate_word = list(candidate.upper())
        candidate_word.sort()

        if target == candidate_word and candidate.lower() != word.lower():
            anagrams.append(candidate)

    return anagrams