class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        OBSTRUCTED = 1
        if obstacle_grid[0][0] == OBSTRUCTED:
            return 0

        rows = len(obstacle_grid); columns = len(obstacle_grid[0])
        dynamic_program = [[0 for _ in range(columns)] for _ in range(rows)]
        dynamic_program[0][0] = 1

        paths = 1
        for row in range(rows):
            if obstacle_grid[row][0] == OBSTRUCTED:
                paths = 0
            dynamic_program[row][0] = paths

        paths = 1
        for column in range(columns):
            if obstacle_grid[0][column] == OBSTRUCTED:
                paths = 0
            dynamic_program[0][column] = paths

        directions = [(1,0), (0,1)]

        for row in range(1, rows):
            for column in range(1, columns):
                if obstacle_grid[row][column] == OBSTRUCTED:
                    continue
                dynamic_program[row][column] = dynamic_program[row-1][column] \
                                             + dynamic_program[row][column-1]

        return dynamic_program[rows-1][columns-1]

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, columns, obstacle = len(grid) - 1, len(grid[0]) - 1, 1
        if grid[0][0] == obstacle:
            return 0
        
        for row in range(rows-1,-1,-1):
            if grid[row+1][-1] == obstacle:
                grid[row][-1] = obstacle
        for column in range(columns-1,-1,-1):
            if grid[-1][column+1] == obstacle:
                grid[-1][column] = obstacle
        
        @cache
        def backtrack(row, column):
            if grid[row][column] == obstacle:
                return 0
            if row == rows or column == columns:
                return 1
            return backtrack(row+1,column) + backtrack(row,column+1)
        
        return backtrack(0,0)
