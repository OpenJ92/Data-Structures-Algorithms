class Solution:
    def combinationSum4(self, numbers: List[int], target: int) -> int:
        @cache
        def backtrack(target):
            if target == 0:
                return 1
            if target <  0:
                return 0

            total = 0
            for number in numbers:
                total += backtrack(target - number)

            return total

        return backtrack(target)
