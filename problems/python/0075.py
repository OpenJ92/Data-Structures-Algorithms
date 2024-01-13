class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def bubblesort(nums):
            for iter_num in range(len(nums)-1,0,-1):
                for idx in range(iter_num):
                    if nums[idx]>nums[idx+1]:
                        temp = nums[idx]
                        nums[idx] = nums[idx+1]
                        nums[idx+1] = temp

        bubblesort(nums)
        return None
