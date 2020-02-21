def distance(strand_a, strand_b):
    """Find the number of difference between two same length strings

    Parameters
    ----------
    strand_a, strand_b : str
    """
    if len(strand_a) == len(strand_b):
        count = 0
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                count += 1
        return count
    else:
        raise ValueError ("length of two inputs should be the same.")

