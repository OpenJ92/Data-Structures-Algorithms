class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = set([num for num in nums if num > 0])
        if not numbers:
            return 1

        maximum = max(numbers)
        minimum = min(numbers)
        length  = len(numbers)

        if length == (maximum - minimum + 1):
            if minimum != 1:
                return 1
            return maximum + 1

        if 1 not in numbers:
            return 1
        for potential in range(minimum, maximum+1):
            if potential not in numbers:
                return potential

