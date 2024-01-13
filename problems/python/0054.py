class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        action = { 'T' : self.top_row
                 , 'R' : self.right_column
                 , 'B' : self.bottom_row
                 , 'L' : self.left_column
                 }

        orders = cycle('TRBL')
        out = []
        for order in orders:
            if not any(matrix):
                break
            elements, matrix = action[order](matrix)
            out = chain(out,elements)
        return out

    def top_row(self, matrix):
        return matrix[0], matrix[1:]

    def bottom_row(self, matrix):
        return matrix[-1][::-1], matrix[:-1]

    def left_column(self, matrix):
        column = []
        nmatrix = []
        for row in matrix:
            col, *nrow = row
            column.append(col)
            nmatrix.append(nrow)
        return column[::-1], nmatrix

    def right_column(self, matrix):
        column = []
        nmatrix = []
        for row in matrix:
            *nrow, col = row
            column.append(col)
            nmatrix.append(nrow)
        return column, nmatrix
