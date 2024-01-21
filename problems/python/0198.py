class Solution:
    def rob(self, value: List[int]) -> int:
        if len(value) == 1:
            return value[0]

        memo = {}
        def dp(house):
            if house == 0:
                return value[house]
            if house == 1:
                return max(value[house], value[house-1])

            if house not in memo:
                memo[house] = max(dp(house-1), value[house] + dp(house-2))

            return memo[house]
        return dp(len(value)-1)

class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (n + 1)
        memo[0] = nums[0]
        if n > 1:
            memo[1] = max(nums[0], nums[1])
            for i in range(2, n):
                memo[i] = max(
                    nums[i] + memo[i-2],
                    0 + memo[i-1]
                )
        return memo[n-1]
