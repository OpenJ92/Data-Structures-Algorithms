class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid); rows = []
        n = len(grid[0]); columns = []

        for row, column in product(range(m), range(n)):
            if grid[row][column]:
                rows.append(row)
                columns.append(column)
            
        def min_distance(positions, origin):
            distance = 0
            for position in positions:
                distance += abs(position - origin)
            return distance
        
        rows.sort()
        columns.sort()
        row = rows[len(rows) // 2]
        column = columns[len(columns) // 2]

        return min_distance(rows, row) + min_distance(columns, column)
