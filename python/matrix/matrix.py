class Matrix:
    """Given a matrix, and be able to get row or columns elements by calling method
        row() or column()
    """

    def __init__(self, matrix_string):
        """
        Parameters
        ----------
        matrix_string : str
            string with all elements for matrix, seperated by '\n' to indicate a 
            different row and seperated by space to indicate elements in each row.
            eg: "1 2 3 4\n5 6 7 8\n9 8 7 6"
        """
        matrix_list = [row.split(" ") for row in matrix_string.split("\n")]
        self.matrix_list = [[int(num) for num in row] for row in matrix_list]

    def row(self, index):
        """call for row elements showing as a list according to row number"""
        return self.matrix_list[index - 1]

    def column(self, index):
        """call for column elements showing as a list according to row number"""
        return [row[index - 1] for row in self.matrix_list]
