import re
from typing import Set


def is_isogram(string):
    """check the input string has repeated letter or not, 
    return True or False.
    
    Note: spaces and hyphens are allowed to appear multiple times"""
    # shirouto: good doc string

    # shirouto: how many times are you scanning the string? I have pointed out
    # repeatedly that this is an expensive operation. You want to minimize
    # it as much as reasonably possible. Just because your code passes the tests
    # it does not mean that you are done. We are also engineers, not only mathematicians:
    # just because the solution is correct (as in it yields the correct response), if
    # it takes too long to run, it is almost as useless as an incorrect solution.

    # shirouto: let's presume that you strip some characters from your string (not that you need
    # actually to do that for this problem), as you attempt to do here. Splitting on regular
    # expressions and then joining is a waste.
    #
    # >>> string.translate({ord(c): None for c in " -"})
    #
    # This will do the same much more efficiently: you go through your string only *once*, not twice.
    string = "".join(re.split("-| ", string)).lower()

    for letter in string:
        # shirouto: this is terrible: you are actually searching again from the start of the string
        # and you do this inside a loop. This is O(n^2). If you compare this with a O(n) implementation
        # that takes 30 minutes to run for a given long string, your implementation would take about
        # ... 15 hours. If O(n) takes 1 hour, your O(n^2) implementation would take about 2 days and a half.
        # Are you willing to wait 2.5 days for a string check when you work on 2 week sprints?

        if string.count(letter) != 1:
            return False

    return True


# shirouto: for reference, here is another possible implementation. What is its asymptotic behavior?
def _is_isogram(string: str) -> bool:
    char_set: Set[str] = set()
    exclude_set: Set[str] = set(" -")

    for c in string.lower():
        if c in exclude_set:
            continue

        if c in char_set:
            return False
        char_set.add(c)

    return True

# shirouto: If you want to formalize the performance checks as unit tests, look into `pytest-benchmark`,
# which can help you write tests against some performance benchmarks. Of course you can always explore
# the asymptotic behavior on your own.
