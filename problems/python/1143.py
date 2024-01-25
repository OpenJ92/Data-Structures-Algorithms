class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_one = len(text1)
        length_two = len(text2)

        @cache
        def backtrack(index, jndex):
            if index == length_one or jndex == length_two:
                return 0

            equal = 0
            if text1[index] == text2[jndex]:
                equal = 1 + backtrack(index+1, jndex+1)
            left  = backtrack(index+1, jndex)
            right = backtrack(index, jndex+1)

            return max(left, right, equal)

        return backtrack(0,0)
