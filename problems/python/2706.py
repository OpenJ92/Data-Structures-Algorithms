class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if (least := prices[0] + prices[1]) <= money:
            money -= least
        return money
