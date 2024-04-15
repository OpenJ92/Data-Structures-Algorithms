class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def binary_search(value, array):
            left, right = 0, len(array) - 1

            while left <= right:
                pivot = left + ((right - left) // 2)
                if array[pivot] >= value:
                    left = pivot + 1
                else:
                    right = pivot - 1

            return left

        rows, length, count = len(grid), len(grid[0]), 0
        for row in grid:
            count += length - binary_search(0, row)
        return count
