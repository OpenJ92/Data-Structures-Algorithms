class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        if n == 1:
          return mat[0][0]

        for i in range(n):
            sum += mat[i][i] + mat[n-i-1][i]

        if n % 2 == 1:
            mid = n // 2
            sum -= mat[mid][mid]

        return sum
