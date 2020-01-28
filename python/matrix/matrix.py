class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string_list = matrix_string.split('\n')

    def row(self, index):
        res = self.matrix_string_list[index-1].split(' ')
        return [int(num) for num in res]

    def column(self, index):
        res = [row.split(' ')[index-1] for row in self.matrix_string_list]
        return [int(num) for num in res]


