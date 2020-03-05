import itertools

# shirouto: I know you do not really use the types for anything besides documentation,
# but since you choose to write them, let's try to do it properly: `dict` is a data constructor.
# The actual type is given by Dict (Mapping is also an immutable option), which is a generic type
# in python typing parlance. So your return type would be Dict[str, int]
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
    

    # shirouto: well, the problem makes no guarantees about the nature of the separator.
    # So why do you? Particularly, what happens if you get unicode strings for example?
    # Do you know? Try calling your function with something like "He said 你好 and he smiled."
    separators = "`~_-+=)(*&^%$#@!:;?/|}]{[>.<,"
    # shirouto: Okay... This is a typical data science task. It is likely an something popping
    # up in most "data science introductory courses" (whatever that may mean). You need to this one
    # at much higher standards than usual. You need to write an implementation that is able to handle
    # a large body of text. You can test it with https://github.com/mahnazkoupaee/WikiHow-Dataset or 
    # any other large body of text.
    # shirouto: First, a contraction is defined by a word contining only *one* "'". What happens
    # when you feed in "I told him D'nin's shoes had cockroaches in them." (that is the name D'nin and
    # the genitive contraction 's)?
    # Second, performance!!! How many times do you parse the string here?
    clean_list = ''.join([c if c not in separators else ' ' for c in sentence ]).lower().split()
    # shirouto: Here? You go again through the list of words, and actually parse each word. Is this really needed?
    strip_apostrophe = [word.strip("'") for word in clean_list]
    
    # shirouto: Ouch. For each word in the text, you call list.count... You know that list.count() is O(n), right?
    # You actually call list.count() even if you come across the same word, every time it appears in the text.
    # Specifically, for "A duck, a hippo, and a fish decided to play the lottery." you call list.count("a") three times.
    # Why? Do you think it will give you a different count? Then you zip this list of numbers with the initial list...
    # to drop all duplicates in the dict() call. Hrm... There is a large amount of waste here.
    return dict(list(zip(strip_apostrophe, [strip_apostrophe.count(word) for word in strip_apostrophe])))

# shirouto: Here is the plan.
# 1. Read over and learn to use a benchmarking tool: pytest-benchmark or timeit should be fine.
# 2. Do not modify this code. Just add to the test harness a benchmark. Note how long your implementation takes.
# 3. Write another implementation (not in place, side by side), and benchmark this one too. Improvement?
# 4. You need at least three versions and benchmarks, but you can keep going as much as you want.
