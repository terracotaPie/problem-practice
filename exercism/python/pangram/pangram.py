import string as s

def is_pangram(string):
    return set([c for c in string.lower() if c in s.ascii_letters]) == set(s.ascii_lowercase)


