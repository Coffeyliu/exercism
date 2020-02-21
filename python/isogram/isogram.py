import re

def is_isogram(string):
    """check the input string has repeated letter or not, 
    return True or False.
    
    Note: spaces and hyphens are allowed to appear multiple times"""

    string = ''.join(re.split('-| ', string)).lower()
    for letter in string:
        if string.count(letter) != 1:
            return False
    return True