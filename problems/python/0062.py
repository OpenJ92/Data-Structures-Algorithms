class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(m, n):
            if not n or not m:
                return 1

            if (m, n) not in memo:
                memo[(m, n)] = dp(m-1, n) + dp(m, n-1)

            return memo[(m, n)]

        return dp(m-1, n-1)
