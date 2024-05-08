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
    def rob(self, value):
        if len(value) < 3:
            return max(value)

        dyn = [0 for _ in range(3)]
        dyn[0], dyn[1] = value[0], max(value[:2])

        for index in range(2, len(value)):
            write, rone, rtwo = index%3, (index-1)%3, (index-2)%3
            dyn[write] = max(value[index] + dyn[rtwo], dyn[rone])

        return dyn[write]
