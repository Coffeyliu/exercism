class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        list_matrix = self.matrix_string.split('\n')
        res = list_matrix[index-1].split()
        return [int(num) for num in res]

    def column(self, index):
        list_matrix = self.matrix_string.split('\n')
        res = [row.split(' ')[index-1] for row in list_matrix]
        return [int(num) for num in res]


