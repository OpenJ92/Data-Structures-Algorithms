class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def valid(row, column):
            return 0 <= row < rows and 0 <= column < columns and grid[row][column] != 0

        def dfs(row, column):
            if not valid(row, column):
                return 0

            maximum, gold = 0, grid[row][column]

            grid[row][column] = 0
            for drow, dcolumn in directions:
                nrow, ncolumn = row+drow, column+dcolumn
                maximum = max(maximum, dfs(nrow, ncolumn))
            grid[row][column] = gold

            return maximum + gold

        maximum = 0
        for row in range(rows):
            for column in range(columns):
                maximum = max(dfs(row, column), maximum)
        return maximum
