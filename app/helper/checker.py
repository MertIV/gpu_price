from difflib import SequenceMatcher

def similarity_check(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_numbers(txt):
    numbers = [int(s) for s in txt.split() if s.isdigit()]
    return numbers