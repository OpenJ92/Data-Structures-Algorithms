class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7

        @cache
        def dfs(nleft, sumleft):
            if nleft == 0 and sumleft == 0: return 1
            if nleft < 0 or sumleft < 0: return 0

            res = 0
            for i in range(1, k+1):
                res += dfs(nleft-1, sumleft - i)
            return res % MOD

        return dfs(n, target)
