class Solution:
    def maxLengthBetweenEqualCharacters(self, string: str) -> int:

        @cache
        def dfs(left, right):
            if string[left] == string[right]:
                return right - left - 1
            return max(dfs(left+1, right),dfs(left, right-1))

        return dfs(0, len(string)-1)

