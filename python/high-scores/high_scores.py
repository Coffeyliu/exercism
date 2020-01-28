def latest(scores):
    copy_scores = scores.copy()
    return copy_scores.pop() if scores != [] else scores


def personal_best(scores):
    return sorted(scores, reverse=True)[0] if scores != [] else scores


def personal_top_three(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[:3] if scores != [] else scores

