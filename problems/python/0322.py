class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def backtrack(amount):
            if amount < 0:
                return 10**4 + 1
            if amount == 0:
                return 0
            
            minimum = 10**4 + 1
            for coin in reversed(coins):
                minimum = min(1 + backtrack(amount - coin), minimum)
            
            return minimum
        
        output = backtrack(amount)
        if output >= 10**4 + 1:
            return -1
        return output
