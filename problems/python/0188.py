class Solution:
    def maxProfit(self, transactions: int, prices: List[int]) -> int:
        length = len(prices)

        @cache
        def backtrack(index, transactions, holding):
            if index == length or transactions == 0:
                return 0

            skip = backtrack(index+1, transactions, holding)
            if holding:
                take = prices[index] + backtrack(index+1, transactions-1, 0)
            else:
                take = -prices[index] + backtrack(index+1, transactions, 1)
            return max(skip, take)

        return backtrack(0, transactions, 0)


class Solution:
    def maxProfit(self, transactions: int, prices: List[int]) -> int:
        length = len(prices)
        dynamic = [[[0] * 2 for _ in range(transactions+1)] for _ in range(length+1)]

        for index in range(length-1,-1,-1):
            for transaction in range(1, transactions+1):
                for holding in range(2): 
                    skip = dynamic[index+1][transaction][holding] 
                    if holding:
                        take = prices[index] + dynamic[index+1][transaction-1][0]
                    else:
                        take = -prices[index] + dynamic[index+1][transaction][1]
                    dynamic[index][transaction][holding] = max(skip, take)
        print(dynamic)
        return dynamic[0][transactions][0]

class Solution:
    def maxProfit(self, transactions: int, prices: List[int]) -> int:
        length = len(prices)
        dynamic = [[[0] * 2 for _ in range(transactions+1)] for _ in range(2)]

        for index in range(length-1,-1,-1):
            read, write = (index + 1) % 2, index % 2
            for transaction in range(1, transactions+1):
                for holding in range(2): 
                    skip = dynamic[read][transaction][holding] 
                    if holding:
                        take = prices[index] + dynamic[read][transaction-1][0]
                    else:
                        take = -prices[index] + dynamic[read][transaction][1]
                    dynamic[write][transaction][holding] = max(skip, take)

        return dynamic[0][transactions][0]

class Solution:
    def maxProfit(self, transactions: int, prices: List[int]) -> int:
        length = len(prices)
        dynamic = [[[0] * 2 for _ in range(2)] for _ in range(length+1)]

        for index in range(length-1,-1,-1):
            for transaction in range(1, transactions+1):
                read, write = (transaction - 1) % 2, transaction % 2
                for holding in range(2): 
                    skip = dynamic[index+1][write][holding] 
                    if holding:
                        take = prices[index] + dynamic[index+1][read][0]
                    else:
                        take = -prices[index] + dynamic[index+1][write][1]
                    dynamic[index][write][holding] = max(skip, take)

        return dynamic[0][transactions % 2][0]
