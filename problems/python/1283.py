class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(nums, threshold, divisor):
            compute = sum(map(lambda num: ceil(num / divisor), nums))
            return compute <= threshold

        upper = max(nums)
        lower = 1
        while upper >= lower:
            middle = lower + ((upper - lower) // 2)
            if check(nums, threshold, middle):
                upper = middle - 1
            else:
                lower = middle + 1

        return lower
