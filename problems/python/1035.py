class Solution:
    def maxUncrossedLines(self, one: List[int], two: List[int]) -> int:
        length, lemgth = len(one), len(two)

        @cache
        def backtrack(top, bottom):
            if top >= length or bottom >= lemgth:
                return 0

            if one[top] == two[bottom]:
                return 1 + backtrack(top+1, bottom+1)
            left = backtrack(top+1, bottom)
            right = backtrack(top, bottom+1)

            return max(left, right)

        return backtrack(0, 0)

class Solution:
    def maxUncrossedLines(self, one: List[int], two: List[int]) -> int:
        length, lemgth = len(one), len(two)
        dynamic = [[0] * (lemgth + 1) for _ in range(length + 1)]

        for top in range(length-1, -1, -1):
            for bottom in range(lemgth-1, -1, -1):
                if one[top] == two[bottom]:
                    dynamic[top][bottom] = 1 + dynamic[top+1][bottom+1]
                    continue
                dynamic[top][bottom] = max(dynamic[top+1][bottom], dynamic[top][bottom+1])

        return dynamic[0][0]

class Solution:
    def maxUncrossedLines(self, one: List[int], two: List[int]) -> int:
        length, lemgth = len(one), len(two)

        (one, length), (two, lemgth) = sorted([(one, length), (two, lemgth)])
        dynamic = [[0] * (length + 1) for _ in range(2)]
        read, write = 0, 1

        for bottom in range(lemgth-1, -1, -1):
            dynamic[write] = [0] * (length + 1)
            for top in range(length-1, -1, -1):
                if one[top] == two[bottom]:
                    dynamic[write][top] = 1 + dynamic[read][top+1]
                    continue
                dynamic[write][top] = max(dynamic[write][top+1], dynamic[read][top])
            read = (read + 1) % 2
            write = (write + 1) % 2

        return dynamic[read][0]
