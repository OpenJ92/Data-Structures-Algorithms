class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        transpose = [[0 for _ in range(n)] for _ in range(m)]

        for i, j in product(range(n), range(m)):
            transpose[j][i] = matrix[i][j]
        
        return transpose
