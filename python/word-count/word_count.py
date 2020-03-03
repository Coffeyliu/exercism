import itertools

def count_words(sentence: str) -> dict:
    """Return a dictionary shows the count of each word of input. 
    
    Note: 
    A number composed of one or more ASCII digits (ie "0" or "1234") OR
    A simple word composed of one or more ASCII letters (ie "a" or "they") OR
    A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
    
    When counting words you can assume the following rules:

    The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
    The count is unordered; the tests will ignore how words and counts are ordered
    Other than the apostrophe in a contraction all forms of punctuation are ignored
    The words can be separated by any form of whitespace (ie "\t", "\n", " ")"""
    

    separators = "`~_-+=)(*&^%$#@!:;?/|}]{[>.<,"
    clean_list = ''.join([c if c not in separators else ' ' for c in sentence ]).lower().split()
    strip_apostrophe = [word.strip("'") for word in clean_list]
    
    return dict(list(zip(strip_apostrophe, [strip_apostrophe.count(word) for word in strip_apostrophe])))


