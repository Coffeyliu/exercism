import string
import timeit
import itertools

#NOTE: I put doc string out of function in order to compare with different versions of function better.
"""Rteurn a dictionary shows the count of each word of input. 
    
    Note: 
    A number composed of one or more ASCII digits (ie "0" or "1234") OR
    A simple word composed of one or more ASCII letters (ie "a" or "they") OR
    A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
    In this exercise, consider a word has apostrophe inside of it as a contraction.(ie "D'nin's" will
    be treated as one word)
    
    When counting words you can assume the following rules:

    The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
    The count is unordered; the tests will ignore how words and counts are ordered
    Other than the apostrophe in a contraction all forms of punctuation are ignored
    The words can be separated by any form of whitespace (ie "\t", "\n", " ")
    """

# def count_words_V1(sentence):
#     separators = "`~_-+=)(*&^%$#@!:;?/|}]{[>.<,"
#     clean_list = ''.join([c if c not in separators else ' ' for c in sentence ]).lower().split()
#     strip_apostrophe = [word.strip("'") for word in clean_list]
#     return dict(list(zip(strip_apostrophe, [strip_apostrophe.count(word) for word in strip_apostrophe])))


# def count_words_V2(sentence):
#     english_word = ''.join([c.lower() if c in string.ascii_letters + string.digits +"'" else ' ' for c in sentence ])
#     strip_apostrophe = [word.strip("'") for word in english_word.split()]
#     strip_apostrophe_set = list(set(strip_apostrophe))
#     return dict(list(zip(strip_apostrophe_set, [strip_apostrophe.count(word) for word in strip_apostrophe_set])))



keep_characters = set(string.ascii_letters + string.digits)
# keep_characters = set(string.ascii_lowercase + string.digits)

def count_words(sentence):
    sentence = sentence.lower()
    on_the_side = ''
    dic = {}
    zzip = itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])

    for (c_before,c,c_after) in zzip:
        if c in keep_characters:
            on_the_side = on_the_side + c
        elif (c == "'") and (c_before and c_after in keep_characters):
            on_the_side = on_the_side + c
        else:
            if on_the_side == '':
                continue
            else:
                if on_the_side not in dic :
                    dic[on_the_side] = 1   
                else:
                    dic[on_the_side] = dic[on_the_side] + 1
            on_the_side = ''
    return dic
                
sentence = "rah$ rah ah ah ah	roma roma ma	ga ga oh la la	want your bad romance"
# print(count_words(sentence))

# print(timeit.timeit('count_words_V1(sentence)', globals=globals()))     #12.003876999999193
# print(timeit.timeit('count_words_V2(sentence)', globals=globals()))     #21.053906000001007
# print(timeit.timeit('count_words(sentence)', globals=globals()))        #9.203510000003007

# take "itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])" out of the for loop.
# print(timeit.timeit('count_words(sentence)', globals=globals()))        #8.946901999999682

# take "(c == "'" and c_before in keep_characters and c_after in keep_characters):" into elif stsatement
# print(timeit.timeit('count_words(sentence)', globals=globals()))        #8.734767000001739

# change ascii_letters to ascii_lowercase
# print(timeit.timeit('count_words(sentence)', globals=globals()))        #9.793047000013757  !!! NOTE: WHY?

# switch back to ascii_letters.
# change (c == "'" and c_before in keep_characters and c_after in keep_characters) to 
# (c == "'") and (c_before and c_after in keep_characters)
# print(timeit.timeit('count_words(sentence)', globals=globals()))        #8.552619000009145








#NOTE: 1. ' ' + string1 is different than string1 + ' '
#NOTE: 2. avoid to use for i in range(len(string)), because it's not O(n) in python
#NOTE: 3. parse in list is O(n), but parse in set is O(log(n))
#NOTE: 4. example to repace of range(len(string)): for (b,c,a) in zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])
