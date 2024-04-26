class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        for row in range(rows-2,-1,-1):

            first, second = inf, inf
            for column in range(columns):
                if grid[row+1][column] < first:
                    second, first = first, grid[row+1][column]
                elif grid[row+1][column] < second:
                    second = grid[row+1][column]

            for column in range(columns):
                mjnimum = first if first != grid[row+1][column] else second
                grid[row][column] += mjnimum

        return min(grid[0])

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        @cache
        def dyn(row, column):
            if row == rows - 1:
                return grid[row][column]

            minimum = inf
            for cplumn in range(columns):
                if cplumn != column:
                    minimum = min(dyn(row+1,cplumn), minimum)

            return grid[row][column] + minimum

        minimum = inf
        for column in range(columns):
            minimum = min(dyn(0, column), minimum)
        return minimum
