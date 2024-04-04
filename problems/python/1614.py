class Solution:
    def maxDepth(self, string: str) -> int:
        open, maximum = 0, 0

        for character in string:
            if character == '(':
                open += 1
                maximum = max(maximum, open)
            if character == ')':
                open -= 1

        return maximum
