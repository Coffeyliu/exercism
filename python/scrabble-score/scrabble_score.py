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
    score_dict = dict(list(itertools.product('a e i o u l n r s t'.split(), [1])) 
                    + list(itertools.product('d g'.split(), [2]))
                    + list(itertools.product('b c m p'.split(), [3]))
                    + list(itertools.product('f h v w y'.split(), [4]))
                    + list(itertools.product('k'.split(), [5]))
                    + list(itertools.product('j x'.split(), [8]))
                    + list(itertools.product('q z'.split(), [10]))
                    )

    return sum(score_dict[c] for c in word.lower())


