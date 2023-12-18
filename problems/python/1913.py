class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        small = math.inf
        smallest = math.inf
        large = -math.inf
        largest = -math.inf

        for num in nums:
            if num > largest:
                large = largest
                largest = num
            else:
                large = max(num, large)

            if num < smallest:
                small = smallest
                smallest = num
            else:
                small = min(num, small)

        return largest * large - smallest * small
