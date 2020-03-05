import itertools

def score(word):
    """calculate score for word according to different value for different letters

    Rule:
    Letter                           Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10
    """
    # shirouto: well, all considering this is fine...
    # However, itertools.product is an overkill really, since you have only one
    # element on the right. Also, concatenating those resulting list is again fine
    # since the lists are short, but really, you would be served better by itertools.chain
    # instead (bypass consuming the generator with list all together). Lastly, those splits,
    # are superfluous since you can directly iterate over a string (and you do that in return statement).
    # Then, if this was used in a game (it is a scoring piece), it will likely be called again and again.
    # Do you really want to recreate this dictionary every time one calls score()?
    # Anyway, here is how I would have written this (notice that there is no need for itertools power tools):
    # {l: v for ls, v in [("aeioulnrst", 1), ("dg", 2), ("bcmp", 3), ("fhvwy", 4), ("k", 5), ("jx", 8), ("qz", 10)] for l in ls}
    score_dict = dict(list(itertools.product('a e i o u l n r s t'.split(), [1])) 
                    + list(itertools.product('d g'.split(), [2]))
                    + list(itertools.product('b c m p'.split(), [3]))
                    + list(itertools.product('f h v w y'.split(), [4]))
                    + list(itertools.product('k'.split(), [5]))
                    + list(itertools.product('j x'.split(), [8]))
                    + list(itertools.product('q z'.split(), [10]))
                    )

    return sum(score_dict[c] for c in word.lower())


