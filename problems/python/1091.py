class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        queue = deque([(0,0,1)])
        seen = set([(0,0)])
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

        def valid(row, col, grid, n):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        while queue:
            row, column, steps = queue.popleft()
            if (row, column) == (n - 1, n - 1):
                return steps

            for dx, dy in directions:
                new_row, new_column = row + dx, column + dy
                if valid(new_row, new_column, grid, n) and (new_row, new_column) not in seen:
                    seen.add((new_row, new_column))
                    queue.append((new_row, new_column, steps + 1))

        return -1

## Alternatively, you can keep using the format from the binary tree problems.
## Then, you wouldn't need to store the number of steps taken so far with each node. 
## You could initialize a variable level before starting the BFS and increment it 
## every time you move up a level (each while loop iteration = one level). When you 
## encounter the target node (n - 1, n - 1), you can return level.

## Look to implement next. 
