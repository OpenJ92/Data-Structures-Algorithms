class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo = {}; length = len(satisfaction)
        def dfs(time, index):
            if index == length:
                return 0

            if (time, index) in memo:
                return memo[(time, index)]

            use_cook = satisfaction[index] * time + dfs(time + 1, index + 1)
            not_cook = dfs(time, index + 1)
            memo[(time, index)] = max(use_cook, not_cook)

            return memo[(time, index)]
        return dfs(1, 0)
