class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(step):
            if step == 0:
                return 0
            if step == 1:
                return 0

            if step not in memo:
                memo[step] = min(dp(step - 1) + cost[step - 1], dp(step - 2) + cost[step - 2])

            return memo[step]

        return dp(len(cost))
