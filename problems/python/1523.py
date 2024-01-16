class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        parity_high = high % 2 != 0
        parity_low  =  low % 2 != 0
        return ceil(diff / 2) + (parity_high and parity_low)
