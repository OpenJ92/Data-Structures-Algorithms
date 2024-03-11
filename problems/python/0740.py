class Solution:
    def deleteAndEarn(self, numbers: List[int]) -> int:
        counter = Counter(numbers)
        numbers = range(min(numbers), max(numbers)+1)

        def safe_access(list, index):
            length = len(list)
            if 0 <= index < length:
                return list[index]
            return math.inf

        @cache
        def backtrack(index):
            if index >= len(numbers):
                return 0

            above = counter[safe_access(numbers, index) + 1]
            below = counter[safe_access(numbers, index) - 1]
            counter[safe_access(numbers, index) - 1] = 0
            counter[safe_access(numbers, index) + 1] = 0
            take = counter[safe_access(numbers, index)] \
                 * safe_access(numbers, index)          \
                 + backtrack(index+2)
            counter[safe_access(numbers, index) - 1] += below
            counter[safe_access(numbers, index) + 1] += above

            skip = backtrack(index+1)
            return max(take, skip)

        return backtrack(0)

