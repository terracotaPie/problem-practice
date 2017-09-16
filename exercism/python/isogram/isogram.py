def is_isogram(string):
    occurence = []
    for char in string:
        if char.isalpha() and char.lower() in occurence:
            return False
        occurence.append(char.lower())
    return True


