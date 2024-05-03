class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def valid(row, column):
            return 0 <= row < rows and 0 <= column < columns and grid[row][column] == 1

        def dfs(start):
            stack = [start]
            while stack:
                row, column = stack.pop()
                grid[row][column] = 0

                for drow, dcolumn in directions:
                    nrow, ncolumn = row+drow, column+dcolumn
                    if valid(nrow, ncolumn):
                        stack.append((nrow, ncolumn))

        for row in range(rows):
            if valid(row, columns-1): dfs((row, columns-1))
            if valid(row, 0): dfs((row, 0))

        for column in range(columns):
            if valid(rows-1, column): dfs((rows-1, column))
            if valid(0, column): dfs((0, column))

        count = 0
        for row in range(1, rows-1):
            for column in range(1, columns-1):
                if valid(row, column):
                    count += 1

        return count

