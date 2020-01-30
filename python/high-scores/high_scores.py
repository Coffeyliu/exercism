def check_poor_user(input_):
    # check input type -- input should be a list
    assert type(input_) == type([]), "Input type error. Input should a list."
    # check elements in input -- elements should be integer
    for ele in input_:
        if type(ele) != type(1):
            raise Exception ("Element in list should be integer.")
    # check empty input
    if not input_:
        raise Exception ("Empty Input Detected, please give another input.")


def latest(scores):
    """return the last element of scores from input
    
    Parameters
    -----------
    scores : list
        list of integers   # TL: by looking at the pytest cases, they want the return is integer,
                                that's why I wrote in here saying 'list of integers'
    
    """
    check_poor_user(scores)
    return scores[-1] 


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
    return max(scores)



def personal_top_three(scores):
    """find the top three scores from the input

    Parameters
    -----------
    scores : list
        list of integers 
    """
    check_poor_user(scores)

    return sorted(scores, reverse=True)[:3]
 
