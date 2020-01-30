# NOTE: factoring this code out is nice: you just call it where needed. Good.
def check_poor_user(input_):
    # check input type -- input should be a list
    # NOTE: I see the intent here. Good. I think the execution can be better if
    # you have instead `assert isinstance(input_, list), "blah, blah"`
    # even better `if not isinstance(input_, list): raise ValueError("list please")
    # END NOTE
    assert type(input_) == type([]), "Input type error. Input should a list."
    # check elements in input -- elements should be integer
    # NOTE: well frankly I wonder why? why restrict your code(pretty generic as it
    # were) to only List[int]? All you need is a list of a type you can order. So basically
    # any class that has defined `__lt__()` or a close friend. This is not needed.
    # END NOTE

    for ele in input_:
        if type(ele) != type(1):
            raise Exception("Element in list should be integer.")
    # check empty input

    # NOTE: actually this test is not needed. First of all, your function is written
    # such that it requires receiving at least one positional parameter. The caller misses
    # to give it one, the runtime will complain before this line gets reached. So the only options
    # for this check to pass are: `None` and `False`. But these guys will already be caught by
    # your `type`-based check ahead. So this is utterly useless code. That will never run.

    if not input_:
        raise Exception("Empty Input Detected, please give another input.")


def latest(scores):
    """return the last element of scores from input
    
    Parameters
    -----------
    scores : list
        list of integers   # TL: by looking at the pytest cases, they want the return is integer,
                                that's why I wrote in here saying 'list of integers'
    
    """
    # NOTE: well, none of the tests do check for `int`. It just happens that they use List[int] for
    # testing. So if your code remains generic (not checking for int as above), it still passes the
    # tests.
    check_poor_user(scores)

    # NOTE: however, you do realize this will blow with IndexError on empty list, right?
    # that may be a bit confusing for the user since he just called a function `latest()`
    # but it is not that bad ;-) You did well here... read the KUDOS next

    return scores[-1]  # KUDOS: yep... simple, elegant, perfectly pythonic. :-)


def personal_best(scores):
    """find the highest score from scores
    
    Parameters
    -----------
    scores : list
        list of integers
    """
    # TL: START
    # max() is O(n) => I calculated
    # sorted() might be O(nlogn) or O(n) ==> according to google. But I need to know more about different sort methods
    # TL: END
    check_poor_user(scores)

    # KUDOS: very nice. And nice response above. Yeah, O(n) is possible usually in some special scenarios though.

    return max(scores)


def personal_top_three(scores):
    """find the top three scores from the input

    Parameters
    -----------
    scores : list
        list of integers 
    """
    check_poor_user(scores)

    return sorted(scores, reverse=True)[
        :3
    ]  # KUDOS: ah, warming my poor heart. Much better.


# SOME GENERAL NOTES:
# * Keep your code as generic as possible. After all Python is dynamical, so enjoy the freedom. So
#   think through what happens with your code before you rush asserting types. For your case here,
#   `personal_top_three` and `personal_best` are straight calling base library functions that already
#   work for lists, only. So they will take care of raising exceptions if argument not list. That should
#   be fine. It is only the `latest` function that may need some help, specifically because IndexError
#   exception for empty lists might be a bit confusing: the user does not specifically pass in any index.
# * Do enable your linting/code formatter in VSCode. It can really help. This is not work, so just
#   see what advice it has for you. If you really disagree with some annoying advice type, you can
#   disable particularly only that advice --- you do not need to disable everything. The linters
#   do allow for configuration.
# * Here is for reference how I would have handled this task:
from typing import List, Optional, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: "Comparable") -> bool:
        ...


A = TypeVar("A", bound=Comparable)
B = TypeVar("B")


def my_personal_best(scores: List[A]) -> A:
    return max(scores)


def my_personal_top_three(scores: List[A]) -> List[A]:
    return sorted(scores, reverse=True)[:3]


def my_latest(scores: List[B]) -> Optional[B]:
    try:
        return scores[-1]
    except IndexError:
        return None


# * Here it is some version that would have earned 5/5 right off the bat:
#   ... well some docstrings would be even nicer :-)

def your_personal_best(scores):
    return max(scores)


def your_personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]


def your_latest(scores):
    return scores and scores[-1]

# * The moral is that whatever style you pick is not that important. The important things are:
#     * Quality of the API you build (well documented, consistent, easy to use, intuitive...)
#     * Efficiency of the implementation (fast, easy on resources, efficient, robust...)
# This is all, really.
