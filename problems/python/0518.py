class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def backtrack(index, amount):
            if index >= len(coins):
                return 0
            if amount == 0:
                return 1
            if amount < 0:
                return 0

            if (index, amount) not in memo:
                take = backtrack(index, amount - coins[index])
                skip = backtrack(index + 1, amount)
                memo[(index, amount)] = take + skip

            return memo[(index, amount)]

        return backtrack(0, amount)

