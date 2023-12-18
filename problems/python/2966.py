class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        out = []
        for index in range(0,len(nums)-2,3):
            if nums[index + 2] - nums[index] <= k:
                out.append([nums[index], nums[index+1], nums[index+2]])
            else:
                return []
        return out
