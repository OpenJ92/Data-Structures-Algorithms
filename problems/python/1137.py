class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 1

            if i not in memo:
                memo[i] = dp(i - 3) + dp(i - 2) + dp(i - 1)

            return memo[i]
        return dp(n)

class Solution:
    def tribonacci(self, n: int) -> int:

        def listbonacci(list, n):
            length = len(list)
            if length > n:
                return list[n]

            for index in range(n - length + 1):
                list[index % length] = sum(list)

            return list[index % length]

        return listbonacci([0,1,1], n)

class Solution:
    def tribonacci(self, n: int) -> int:

        def listbonacci(list):
            def bonacci(n):
                length = len(list)

                if length > n:
                    return list[n]

                for index in range(n - length + 1):
                    list[index % length] = sum(list)

                return list[index % length]
            return bonacci

        bonacci = listbonacci([0,1,1])
        return bonacci(n)
