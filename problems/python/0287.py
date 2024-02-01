class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        current = 0; last = -1
        for num in nums:
            last = current
            current ^= 1 << num
            if last > current:
                return num
        return -1

