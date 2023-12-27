class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        max_consecutive = -math.inf

        for pointer in range(len(nums)):
            if nums[pointer] == 1:
                consecutive += 1
                max_consecutive = max(consecutive, max_consecutive)
            if nums[pointer] == 0:
                consecutive = 0

        return max_consecutive if max_consecutive != -math.inf else 0
