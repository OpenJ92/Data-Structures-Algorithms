class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        rows = len(grid)
        columns = len(grid[0])

        valid = set()
        start = None
        end   = None

        paths = 0

        for row, column in product(range(rows), range(columns)):
            match grid[row][column]:
                case 0: valid.add((row,column))
                case 1: start = (row,column)
                case 2:
                    end = (row,column)
                    valid.add(end)
                case _: continue

        def dfs(row, column):
            nonlocal paths

            if (row, column) == end:
                if valid == set():
                    paths += 1
                    return

            for drow, dcol in directions:
                nrow, ncol = row+drow, column+dcol
                if (nrow, ncol) in valid:
                    valid.remove((nrow, ncol))
                    dfs(nrow, ncol)
                    valid.add((nrow, ncol))

        dfs(*start)
        return paths
