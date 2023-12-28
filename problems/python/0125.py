class Solution:
    def isPalindrome(self, string: str) -> bool:
        left = 0
        right = len(string) - 1
        string = string.lower()

        while left < right:
            if not string[right].isalnum():
                right -= 1
                continue
            if not string[left].isalnum():
                left += 1
                continue

            if string[left] != string[right]:
                return False
            right -= 1
            left  += 1

        return True

