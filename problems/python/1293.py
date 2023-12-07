class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        OBSTACLE = 1
        OPEN     = 0
        rows     = len(grid)
        columns  = len(grid[0])
        moves = [(1,0), (0,1), (-1,0), (0,-1)]

        if k >= rows + columns - 2:
            return rows + columns - 2

        def valid_(row, column):
            return (0 <= row < rows) and (0 <= column < columns)

        queue = deque([(0,0,k,0)])
        seen = set([(0,0,k)])
        while queue:
            row, col, k, steps = queue.popleft()
            if (row, col) == (rows-1, columns-1):
                return steps

            for drow, dcol in moves:
                new_row, new_col = row+drow, col+dcol

                if not valid_(new_row, new_col):
                    continue

                if grid[new_row][new_col] == OPEN:
                    if (new_row, new_col, k) not in seen:
                        queue.append((new_row, new_col, k, steps+1))
                        seen.add((new_row, new_col, k))
                elif k and (new_row, new_col, k - 1) not in seen:
                    queue.append((new_row, new_col, k-1, steps+1))
                    seen.add((new_row, new_col, k-1))
        return -1

