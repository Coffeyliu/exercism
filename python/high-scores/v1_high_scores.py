def latest(scores):
    # FB: START
    #
    # * ouch. This is bit painful to see. Why do you copy the entire list? This is
    #   a very expensive operation. The CPU will need to walk the entire list, allocate
    #   new memory and then copy the values over. You are not only wasting CPU time but also
    #   memory by the way. Python lists are not quite... lists. They are a form of flexible
    #   arrays. Both in under the hood implementation and in their API (functions available in
    #   the standard library for them. So, frankly this task is not that inspired, but looking
    #   at the test case available, it appears that one is supposed to add a new score at...
    #   the bottom of the list. So how can you get the last element in a list? What happens
    #   if one indexes a list with negative integer? Make it nicer please.
    #
    # * Do heed the comments I made to the next function. The general concepts contained in there
    #   may apply here too: formal parameter handling, API definition and exception handling, how
    #   to check for empty lists.
    #
    # FB: END
    copy_scores = scores.copy()

    return copy_scores.pop() if scores != [] else scores


def personal_best(scores):
    # FB: START
    # First, your code does the minimum: it works in as much as the tests concerned
    # However, there are some pointers to make it better:
    #
    # * Python is a strongly typed dynamical language (please do check wikipedia for an
    #   an explanation as to what this means). A consequence of that is that `scores` can be
    #   anything. The function definition places no constraints on the nature of `scores`.
    #   It could be an `int`, a `string`, a `dict`... anything. The user of your function will
    #   not have any idea what it should be. So, you like a good fellow that you are, do not
    #   want to let them confused. The function call will work no matter what the type of the
    #   `scores` is, but... later on it might blow with exceptions. There are multiple options
    #   for how to handle that, so you do not scare the poor user out of their wits. To name
    #   a few: docstrings (your friends by now), runtime checks for values with custom exceptions
    #   (this was hinted at in the text of this problem actually), type annotations (they will not
    #   prevent one from shooting themselves in the foot, but at least you give them a heads up),
    #   defining custom (sub-)classes and use them to implement/document/handle wrong input (a bit
    #   more involved but worth in some cases. Anyway, please pick on way and handle the cases where
    #   the user of your function calls it with things that your function is meant to handle
    #
    # * you just need to return the maximum element. Not to sort the entire list. The latter is more
    #   expensive. Check the complexity of sorting algorithms versus max algorithms and let me know
    #   how they compare. Yes, I want big `O` or big `Omega` notation. Furthermore, how could you make
    #   make your code faster in this case?
    #
    # * the way you check for whether the `scores` list is empty works, but it is not so pretty now: it is
    #   a bit of a waste since you create an empty list only to compare it to your `scores`. There is really
    #   no need for the former. Simply just checking `if scores else...` should be plenty. In the bigger
    #   picture, there is no reason to throw back at the poor user their empty list. Is that nice? A nice
    #   exception with a tailored message should be more polite, don't you think?
    #
    # FB: END

    return sorted(scores, reverse=True)[0] if scores != [] else scores


def personal_top_three(scores):
    # FB: START
    # First, your code does the minimum: it works in as much as the tests concerned
    # However, there are some pointers to make it better:
    #
    # * so what happens if the list has less then 3 elements? How could you improve your code then? Do heed
    #   the comments above. They already contain a few suggestions that are pertinent here too.
    #
    # FB: END
    sorted_scores = sorted(scores, reverse=True)

    return sorted_scores[:3] if scores != [] else scores
