class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        size = len(matrix)

        def valid(row, column):
            return 0 <= row < size and 0 <= column < size

        @cache
        def dfs(row, column):
            if row == size - 1:
                return 0

            minimum = math.inf
            for next in [-1, 0, 1]:
                if valid(row+1, next+column):
                    value = matrix[row+1][next+column]
                    minimum = min(value + dfs(row+1,column+next), minimum)

            return minimum

        minimum = math.inf
        for column in range(size):
            value = matrix[0][column]
            minimum = min(value + dfs(0, column), minimum)
        return minimum
