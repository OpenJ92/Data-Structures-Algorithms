class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        constructions = set()
        def valid(num):
            return 0 <= num <= 9

        def dfs(n, index, candidate):
            if n == 1:
                number = int("".join(map(lambda num: str(num), candidate[:])))
                if number not in constructions:
                    constructions.add(number)
                return

            plausible_up, plausible_down = index - k, index + k

            if valid(plausible_down):
                candidate.append(plausible_down)
                dfs(n - 1, plausible_down, candidate)
                candidate.pop()
            if valid(plausible_up):
                candidate.append(plausible_up)
                dfs(n - 1, plausible_up, candidate)
                candidate.pop()
            return

        for start in range(1, 10):
            dfs(n, start, [start])

        return constructions
