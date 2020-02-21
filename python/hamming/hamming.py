def distance(strand_a, strand_b):
    """Find the number of difference between two same length strings

    Parameters
    ----------
    strand_a, strand_b : str
    """

    if len(strand_a) == len(strand_b):
        count = 0
        # shirouto: most of the time, if you see something like this in python
        # you better start looking for other ways: you really do not need
        # to use indeces to iterate through a sequence in python --- almost
        # always there are ways around. Why? Because it makes for less
        # readable code, exposes you to boundary issues (not particularly here)
        # and most importantly, you are likely to end up with not so efficient code
        # (and the latter does apply here). How many times have you computed the length
        # of the string in this code? You already know that is O(n), right? We have talked
        # about this previously...

        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                count += 1

        return count
    else:
        raise ValueError("length of two inputs should be the same.")


# shirouto: here is one way to approach this task

from itertools import starmap, zip_longest


def _cmp(x: str, y: str) -> bool:
    if x and y:
        return x != y
    else:
        raise ValueError("Failed to compare")


def _distance(a: str, b: str) -> int:
    return sum(starmap(_cmp, zip_longest(a, b)))

