class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)

        def recurrence(n, memo):
            if n == 2:
                return 2
            if n == 1:
                return 1

            if n - 1 not in memo:
                memo[n-1] = recurrence(n-1, memo)

            if n - 2 not in memo:
                memo[n-2] = recurrence(n-2, memo)

            return memo[n-1] + memo[n-2]

        return recurrence(n, memo)
