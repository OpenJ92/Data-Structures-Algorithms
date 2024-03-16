class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = defaultdict(lambda: None)
        for index, num in enumerate(nums):
            memo[target - num] = index

        for jndex, num in enumerate(nums):
            if memo[num] != None and memo[num] != jndex:
                return [memo[num], jndex]
