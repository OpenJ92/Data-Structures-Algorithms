class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        rows = len(grid); columns = len(grid[0])

        for row, column in product(range(rows), range(columns)):
            count[grid[row][column]] += 1

        out = [0, 0]
        for element in range(1, rows*columns + 1):
            if count[element] == 0:
                out[1] = element
            if count[element] == 2:
                out[0] = element

        return out
