# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binary_matrix: 'BinaryMatrix') -> int:
        rows, columns = binary_matrix.dimensions()
        def binary_search(row):
            left  = 0
            right = columns - 1

            if not binary_matrix.get(row, right):
                return math.inf

            while left <= right:
                middle = left + ((right - left) // 2)
                if binary_matrix.get(row, middle) == 1:
                    right = middle - 1
                else:
                    left = middle + 1
            return left

        leftmost = math.inf
        for row in range(rows):
            column   = binary_search(row)
            leftmost = min(column, leftmost)

        return leftmost if leftmost != math.inf else -1
