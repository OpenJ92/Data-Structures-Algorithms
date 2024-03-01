class Solution:
    def maximumOddBinaryNumber(self, string: str) -> str:
        counter = Counter(string)
        return "1"*(counter["1"] - 1) + "0"*counter["0"] + "1"
