class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)-1; columns = len(triangle[-1])-1

        for row in range(rows-1, -1, -1):
            for column in range(row+1):
                triangle[row][column] += min(triangle[row+1][column], triangle[row+1][column+1])

        return triangle[0][0]
