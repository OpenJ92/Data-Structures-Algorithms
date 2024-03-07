class TLE:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows    = len(matrix) - 1
        columns = len(matrix[0]) - 1
        heights = min(rows, columns) + 1
        maximum = any(map(lambda row: '1' in row, matrix))

        if not maximum:
            return 0

        dynamic_program = [[['0' for _ in range(columns+1)] for _ in range(rows+1)] for _ in range(heights)]
        dynamic_program[0] = matrix

        for height in range(heights):
            for row in range(rows-height-1, -1, -1):
                for column in range(columns-height-1, -1, -1):
                    if all([
                        dynamic_program[height][row][column]     == '1'
                    ,   dynamic_program[height][row+1][column]   == '1'
                    ,   dynamic_program[height][row][column+1]   == '1'
                    ,   dynamic_program[height][row+1][column+1] == '1'
                    ]):
                        dynamic_program[height+1][row][column] = '1'
                        maximum = max(maximum, height+2)

        return maximum ** 2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows    = len(matrix) - 1
        columns = len(matrix[0]) - 1
        heights = min(rows, columns) + 1
        maximum = any(map(lambda row: '1' in row, matrix))

        if not maximum:
            return 0

        dynamic_program = [[['0' for _ in range(columns+1)] for _ in range(rows+1)] for _ in range(heights)]
        dynamic_program[0] = matrix

        for height in range(heights):
            for row in range(rows-height-1, -1, -1):
                for column in range(columns-height-1, -1, -1):
                    if dynamic_program[height][row][column]     == '1' \
                    and all([
                       dynamic_program[height][row+1][column]   == '1'
                    ,  dynamic_program[height][row][column+1]   == '1'
                    ,  dynamic_program[height][row+1][column+1] == '1'
                    ]):
                        dynamic_program[height+1][row][column] = '1'
                        maximum = max(maximum, height+2)

        return maximum ** 2

class Optimized:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows    = len(matrix) - 1
        columns = len(matrix[0]) - 1
        heights = min(rows, columns) + 1
        maximum = any(map(lambda row: '1' in row, matrix))

        if not maximum:
            return 0

        dynamic_program = [[['0' for _ in range(columns+1)] for _ in range(rows+1)] for _ in range(heights)]
        dynamic_program[0] = matrix

        for height in range(heights):
            for row in range(rows-height-1, -1, -1):
                for column in range(columns-height-1, -1, -1):
                    if  dynamic_program[height][row][column]     == '1' \
                    and dynamic_program[height][row+1][column]   == '1' \
                    and dynamic_program[height][row][column+1]   == '1' \
                    and dynamic_program[height][row+1][column+1] == '1' :
                        dynamic_program[height+1][row][column] = '1'
                        maximum = max(maximum, height+2)

        return maximum ** 2
