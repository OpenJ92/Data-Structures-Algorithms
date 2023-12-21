class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows    = len(grid)
        columns = len(grid[0])

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < columns

        def safe_access(default, grid, row, col):
            if not valid(row, col):
                return math.inf
            return grid[row][col]

        def access(row, col):
            return safe_access(0,grid,row,col)

        for row in range(rows-1, -1, -1):
            for column in range(columns-1, -1, -1):
                right  = access(row,column+1)
                bottom = access(row+1,column)
                if right == math.inf and bottom == math.inf:
                    val = 0
                else:
                    val = min(right, bottom)
                grid[row][column] += val

        return grid[0][0]
