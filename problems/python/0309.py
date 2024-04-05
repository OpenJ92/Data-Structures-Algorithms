class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0

        @cache
        def backtrack(index, holding):
            if index >= length:
                return 0

            skip = backtrack(index + 1, holding)
            if holding:
                take = prices[index] + backtrack(index + 2, 0)
            else:
                take = -prices[index] + backtrack(index + 1, 1)

            return max(skip, take)

        return backtrack(0, 0)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        dynamic = [[0] * 2 for _ in range(length + 2)]

        for index in range(length-1,-1,-1):
            for holding in range(2):
                skip = dynamic[index+1][holding]
                if holding:
                    take = prices[index] + dynamic[index+2][0]
                else:
                    take = -prices[index] + dynamic[index+1][1]
                dynamic[index][holding] = max(take, skip)

        return dynamic[0][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        dynamic = [[0] * 2 for _ in range(3)]

        for index in range(length-1,-1,-1):
            two, one, write = (index + 2) % 3, (index + 1) % 3, index % 3
            for holding in range(2):
                skip = dynamic[one][holding]
                if holding:
                    take = prices[index] + dynamic[two][0]
                else:
                    take = -prices[index] + dynamic[one][1]
                dynamic[write][holding] = max(take, skip)

        return dynamic[0][0]

