class Solution:
    def lengthOfLastWord(self, string: str) -> int:
        left, right = len(string) - 1, len(string) - 1

        while right >= 0 and string[right] == ' ':
            left -= 1
            right -= 1
        
        while left >= 0 and string[left] != ' ':
            left -= 1
        
        return right - left
