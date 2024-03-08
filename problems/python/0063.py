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

