class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        for num in nums:
            cache[num] += 1

        def dfs(value):
            stack = deque([(value, 0)])

            while stack:
                node, steps = stack.pop()
                if node < 0:
                    continue
                if node == 0:
                    return steps
                stack.append((node - 2, steps + 1))
                stack.append((node - 3, steps + 1))
            return -1

        result = 0
        for _, value in cache.items():
            operations = dfs(value)
            if operations == -1:
                return -1
            result += operations
        return result
