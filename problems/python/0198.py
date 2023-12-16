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
