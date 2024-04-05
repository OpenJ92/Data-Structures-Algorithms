class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        if length <= 1:
            return 0

        @cache
        def backtrack(index, holding):
            if index == length:
                return 0

            skip = backtrack(index+1, holding)
            if holding:
                take = prices[index] - fee + backtrack(index+1, 0)
            else:
                take = -prices[index] + backtrack(index+1, 1)

            return max(skip, take)

        return backtrack(0, 0)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        dynamic = [[0] * 2 for _ in range(length + 1)]

        for index in range(length-1,-1,-1):
            for holding in range(2):
                skip = dynamic[index+1][holding]
                if holding:
                    take = prices[index] - fee + dynamic[index+1][0]
                else:
                    take = -prices[index] + dynamic[index+1][1]
                dynamic[index][holding] = max(skip, take)

        return dynamic[0][0]


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        dynamic = [[0] * 2 for _ in range(2)]

        for index in range(length-1,-1,-1):
            read, write = (index + 1) % 2, index % 2
            for holding in range(2):
                skip = dynamic[read][holding]
                if holding:
                    take = prices[index] - fee + dynamic[read][0]
                else:
                    take = -prices[index] + dynamic[read][1]
                dynamic[write][holding] = max(skip, take)

        return dynamic[0][0]
