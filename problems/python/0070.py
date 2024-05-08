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

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        dyn = [0 for _ in range(3)]
        dyn[0], dyn[1] = 1, 2

        for index in range(2, n):
            dyn[index%3] = dyn[(index-1)%3] + dyn[(index-2)%3]

        return dyn[index%3]

