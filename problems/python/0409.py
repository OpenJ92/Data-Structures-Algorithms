class Solution:
    def longestPalindrome(self, string: str) -> int:
        counter, size, middle = Counter(string), 0, False

        for _, frequency in counter.items():
            _, remainder = divmod(frequency, 2)
            size += frequency - remainder
            middle |= remainder

        return size + middle
