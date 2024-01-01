## O(n**2) time/space
class Solution:
    def maxLengthBetweenEqualCharacters(self, string: str) -> int:

        @cache
        def dfs(left, right):
            if string[left] == string[right]:
                return right - left - 1
            return max(dfs(left+1, right),dfs(left, right-1))

        return dfs(0, len(string)-1)

## O(n) time/space
class Solution:
    def maxLengthBetweenEqualCharacters(self, string: str) -> int:
        memo = {}

        for index, char in enumerate(string):
            if char not in memo:
                memo[char] = (index, index)
                continue
            start, end = memo[char]
            memo[char] = (start, index)

        max_length = -1
        for _, (start, end) in memo.items():
            max_length = max(end - start - 1, max_length)

        return max_length
