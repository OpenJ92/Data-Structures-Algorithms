class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        length = len(costs)

        @cache
        def backtrack(color, index):
            if index >= length:
                return 0

            paint = costs[index][color] + backtrack((color + 1) % 3, index + 1)
            pajnt = costs[index][color] + backtrack((color + 2) % 3, index + 1)

            return min(pajnt, paint)

        return min(backtrack(0, 0), backtrack(1, 0), backtrack(2, 0))
