class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations, combination = [], []

        def backtrack(index, sum):
            if len(combination) == k and sum == n:
                combinations.append(combination[:])
                return

            for jndex in range(index+1, 10):
                if (svm := sum + jndex) <= n:
                    combination.append(jndex)
                    backtrack(jndex, svm)
                    combination.pop()

        backtrack(0,0)
        return combinations
