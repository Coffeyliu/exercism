# FIXME: no class docstrings? no method docstrings? :-)
class Matrix:
    def __init__(self, matrix_string):
        # FIXME: well, there are multiple ways to represent a matrix
        # each of which is optimized for some particular usage while
        # being relatively weak for other types of usage. In this case,
        # you are told nothing about the intended usage, so you can choose,
        # but the representation you chose is a very very unlikely to be
        # optimal for something. Since this is a numerical matrix, one would
        # expect that one keeps calling its methods again and again after
        # instantiation. But if you keep your matrix as a list of strings (rows),
        # you will have to keep parsing the strings again and again for each call to
        # row() and column(). That is wasteful. Why not parse it fully the only
        # once in the constructor __init__() and avoid calling split() and int()
        # multiple times on every method call?
        self.matrix_string_list = matrix_string.split("\n")

    def row(self, index):
        res = self.matrix_string_list[index - 1].split(" ")

        return [int(num) for num in res]

    def column(self, index):
        # FIXME: for small matrices, it doesn't make much of a difference, but
        # there is no note of what dimensions the input matrix will have: as the
        # matrix is larger, the cost of iterating twice through as you
        # do here becomes noticeable (once to build res, and then to convert it to int).
        # However, I advice you fix __init__ first before you start on this one (who knows?
        # you might not need to fix this after all :-) ).
        res = [row.split(" ")[index - 1] for row in self.matrix_string_list]

        return [int(num) for num in res]

# KUDOS: I really liked that your code can handle non-square matrices. Good job.
