class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        houses = len(costs)
        paints = len(costs[0])

        @cache
        def backtrack(index, color):
            if index >= houses:
                return 0

            cost = math.inf
            for paint in range(1, paints):
                cost = min(cost, costs[index][color] + backtrack(index+1, (color + paint) % paints))
            return cost

        return min(backtrack(0, paint) for paint in range(paints))
