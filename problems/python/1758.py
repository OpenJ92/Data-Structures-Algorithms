class Solution:
    def minOperations(self, string: str) -> int:
        length      = len(string)
        alternation = cycle(['1','0'])

        count = 0
        for proper, bit in zip(alternation, string):
            if bit != proper:
                count += 1

        return min(count, length - count)
