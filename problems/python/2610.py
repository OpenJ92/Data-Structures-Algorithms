class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = []
        for num in nums:
            self.insert(num, matrix)
        return matrix

    def insert(self, num, matrix):
        row = 0; length = len(matrix)
        while row < length:
            if num not in matrix[row]:
                matrix[row].add(num)
                return matrix
            row += 1
        matrix.append(set([num]))
        return matrix
