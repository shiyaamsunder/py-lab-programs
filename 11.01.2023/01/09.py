string = "this is a string"

vowels_set = set(("a","i", "e", "o", "u"))

consonants = [i for i in string if i not in vowels_set and i != ' ']

print("".join(consonants))
