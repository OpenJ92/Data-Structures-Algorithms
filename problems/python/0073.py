class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        zrows = set()
        zcolumns = set()

        for row, column in product(range(rows), range(columns)):
            if matrix[row][column] == 0:
                zrows.add(row)
                zcolumns.add(column)

        for row in zrows:
            for column in range(columns):
                matrix[row][column] = 0

        for column in zcolumns:
            for row in range(rows):
                matrix[row][column] = 0

        return
