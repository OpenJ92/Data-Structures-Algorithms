class Solution:
    def reverseString(self, string: List[str]) -> None:
        left, right = 0, len(string) - 1

        while left <= right:
            string[left], string[right] = string[right], string[left]
            left, right = left + 1, right - 1

        return string

