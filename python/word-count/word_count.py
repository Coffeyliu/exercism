import string
import timeit
import itertools 
from collections import defaultdict
from rust import rust_word_count

#set number = 1000
sentence = "rah$ rah ah ah ah	roma roma ma	ga ga oh la la	want your bad romance"*1000
def time_run(func, runs=1000):
    func_name = func.__name__
    print("{}:".format(func_name), timeit.timeit("{}(sentence)".format(func_name), globals=globals(), number=runs))


# CPython extension module (rust)
time_run(rust_word_count)

# from numba import njit, types

# # numba has very poor performance with strings: it is optimized for numerical code
# # but just as a reference here, a numbe based implementation
# # you can refer at later on
a, z = ord("a"), ord("z")
d1, d0 = ord("1"), ord("0")
ap = ord("'")

# @njit(types.boolean(types.int16))
def keep(c):
    return (a <= c and c <= z) or (d1 <= c and c <= d0)

# @njit(types.DictType(*(types.unicode_type,types.int64))(types.unicode_type))
def count_words_work(sentence):
    chars = [ord(c) for c in sentence.lower()+"\n"]
    word = ""
    # NOTE: a hack to go around not having a type declaration mechanism to handle 
    # to mitigate the failures in the type inference step
    count = {} # {"":0} 

    for i, c in enumerate(chars):
        if keep(c) or (c == ap and word and keep(chars[i+1])):
            word += chr(c)
        elif word:
            count[word] = 1 + (word in count and count[word])
            word = ""

    return count
time_run(count_words_work)


# #the first version of successful pytest
keep_characters = set(string.ascii_letters + string.digits)
def count_words_origin(sentence):
    sentence = sentence.lower()
    on_the_side = ''
    dic = {}
    zzip = itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])

    for (c_before,c,c_after) in zzip:
        if c in keep_characters or (c == "'" and c_before in keep_characters and c_after in keep_characters):
            on_the_side = on_the_side + c
        else:
            if on_the_side == '':
                continue
            else:
                if on_the_side in dic:
                    dic[on_the_side] = dic[on_the_side] + 1
                else:
                    dic[on_the_side] = 1
                on_the_side = ''

    return dic
time_run(count_words_origin)


#------------------ 1. change string.ascii_letters to string.ascii_lowercase ------------------
keep_characters = set(string.ascii_lowercase + string.digits)
def count_words_lowercase(sentence):
    sentence = sentence.lower()
    on_the_side = ''
    dic = {}
    zzip = itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])

    for (c_before,c,c_after) in zzip:
        if c in keep_characters or (c == "'" and c_before in keep_characters and c_after in keep_characters):
            on_the_side = on_the_side + c
        else:
            if on_the_side == '':
                continue
            else:
                if on_the_side in dic:
                    dic[on_the_side] = dic[on_the_side] + 1
                else:
                    dic[on_the_side] = 1
                on_the_side = ''

    return dic
time_run(count_words_lowercase)



#------------------ 2. change d={} to d=defaultdict(int) ------------------
keep_characters = set(string.ascii_letters + string.digits)
def count_words_defaultdict(sentence):
    sentence = sentence.lower()
    on_the_side = ''
    dic = defaultdict(int)
    zzip = itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])

    for (c_before,c,c_after) in zzip:
        if c in keep_characters or (c == "'" and c_before in keep_characters and c_after in keep_characters):
            on_the_side = on_the_side + c
        else:
            if on_the_side == '':
                continue
            else:
                dic[on_the_side] = dic[on_the_side] + 1
                on_the_side = ''

    return dic
time_run(count_words_defaultdict)




#------------------ 3.change on_the_side from str to list ------------------
keep_characters = set(string.ascii_letters + string.digits)
def count_words_list(sentence):
    sentence = sentence.lower()
    on_the_side = []
    dic = {}
    zzip = itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])

    for (c_before,c,c_after) in zzip:
        if c in keep_characters or (c == "'" and c_before in keep_characters and c_after in keep_characters):
            on_the_side.append(c)
        else:
            if on_the_side == []:
                continue
            else:
                word = ''.join(on_the_side)

                if word in dic:
                    dic[word] = dic[word] + 1
                else:
                    dic[word] = 1
                on_the_side = []

    return dic
time_run(count_words_list)


#------------------ 4. change if on_the_side =='' to if on_the side and swap the braches thereafter.   ------------------
keep_characters = set(string.ascii_letters + string.digits)
def count_words_swap(sentence):
    sentence = sentence.lower()
    on_the_side = ''
    dic = {}
    zzip = itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])

    for (c_before,c,c_after) in zzip:
        if c in keep_characters or (c == "'" and c_before in keep_characters and c_after in keep_characters):
            on_the_side = on_the_side + c
        else:
            if on_the_side:
                if on_the_side in dic:
                    dic[on_the_side] = dic[on_the_side] + 1
                else:
                    dic[on_the_side] = 1
                on_the_side = ''
            else:
                continue

    return dic
time_run(count_words_swap)

#------------------ 5. change zzip with keep (c and c_after)   ----------------HAS ERROR--
# keep_characters = set(string.ascii_letters + string.digits)
# def count_words(sentence):
#     sentence = sentence.lower()
#     on_the_side = ''
#     dic = {}
#     zzip = itertools.zip_longest(sentence, sentence[1:])

#     for (c,c_after) in zzip:
#         if c in keep_characters or (c == "'" and c_after in keep_characters):
#             on_the_side = on_the_side + c
#         else:
#             if on_the_side == '':
#                 continue
#             else:
#                 if on_the_side in dic:
#                     dic[on_the_side] = dic[on_the_side] + 1
#                 else:
#                     dic[on_the_side] = 1
#                 on_the_side = ''
#     return dic


# #---------------------------------------------------------HAS ERROR-------------
# keep_characters = set(string.ascii_lowercase + string.digits)
# def count_words(sentence):
#     sentence = sentence.lower()
#     on_the_side = ""
#     dic = defaultdict(int)
    
#     for c, c_after in zip_longest(sentence, sentence[1:]):
#         if c in keep_characters:
#             on_the_side += c
#         elif (c == "'") and on_the_side and (c_after in keep_characters):
#             on_the_side += c
#         elif on_the_side:
#            # end of word, if any
#             dic[on_the_side] += 1
#             on_the_side = ""
#     return dic


#------------------ 6.back to str for on_the_side & defaultdict & swap & lowercase(good for larget dataset)----------BEST APPROACH FOR NOW--
keep_characters = set(string.ascii_lowercase + string.digits)
def count_words_best(sentence):
    sentence = sentence.lower()
    on_the_side = ''
    dic = defaultdict(int)
    zzip = itertools.zip_longest(itertools.chain([None], sentence), sentence, sentence[1:])

    for (c_before,c,c_after) in zzip:
        if c in keep_characters or (c == "'" and c_before in keep_characters and c_after in keep_characters ):
            on_the_side = on_the_side + c
        else:
            if on_the_side:
                dic[on_the_side] += 1
                on_the_side = ''
            else:
                continue

    return dic
time_run(count_words_best)


keep_characters = set(string.ascii_lowercase + string.digits)
def count_words_zip2(sentence):
    sentence = sentence.lower()
    on_the_side = ''
    dic = defaultdict(int)

    for (c,c_after) in itertools.zip_longest(sentence, sentence[1:]):
        if c in keep_characters or (c == "'" and on_the_side and c_after in keep_characters):
            on_the_side = on_the_side + c
        elif on_the_side:
            dic[on_the_side] += 1
            on_the_side = ''

    if on_the_side: dic[on_the_side] += 1

    return dic
time_run(count_words_zip2)



"""
RESULTS: Best is the best :D

(.venv_exer) root@ZHOBL-10DKPQ2:~/exercism/python/word-count# python word_count.py 
count_words_origin:  2.092539000001125
count_words_lowercase:  2.0533570000006875
count_words_defaultdict:  1.9176990000014484
count_words_list:  2.6344869999993534
count_words_swap:  1.95707499999844
count_words_best:  1.885603999999148


(.venv_exer) root@ZHOBL-10DKPQ2:~/exercism/python/word-count# python word_count.py 
count_words_origin:  1.9086279999974067
count_words_lowercase:  1.960218000000168
count_words_defaultdict:  1.8306570000022475
count_words_list:  2.5145809999994526
count_words_swap:  1.892480999998952
count_words_best:  1.822345000000496


(.venv_exer) root@ZHOBL-10DKPQ2:~/exercism/python/word-count# python word_count.py 
count_words_origin:  1.9719239999976708
count_words_lowercase:  1.9162189999988186
count_words_defaultdict:  2.221187999999529
count_words_list:  2.535228000000643
count_words_swap:  2.40890600000057
count_words_best:  1.8334450000002107



"""
