class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binary_search(array, target):
            left, right = 0, len(array) - 1

            while left <= right:
                pivot = left + ((right - left) // 2)
                if array[pivot][0] >= target:
                    right = pivot - 1
                else:
                    left = pivot + 1

            return left

        length = len(intervals)
        for index in range(length):
            intervals[index] = [*intervals[index], index]
        intervals.sort()

        output, lower = [-1] * length, 0
        for _, upper, index in intervals:
            jndex = binary_search(intervals, upper)
            if jndex < length and upper <= intervals[jndex][lower]:
                output[index] = intervals[jndex][-1]

        return output
