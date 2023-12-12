class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        nums = [-num for num in nums]
        heapify(nums)
        operations = 0

        while target > 0:
            top = heappop(nums) / 2
            target += top
            heappush(nums, top)
            operations += 1

        return operations
