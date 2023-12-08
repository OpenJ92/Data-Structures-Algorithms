class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        columns = len(maze[0])
        row, col = entrance

        FLOOR = '.'
        WALL  = '+'

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def at_exit(row, col):
            return row == (rows - 1) or row == 0 or col == (columns - 1) or col == 0

        def is_valid(row, col):
            return  0 <= row < rows and 0 <= col < columns and maze[row][col] != WALL

        queue = deque([(row, col, 0)])
        state = set([(row, col)])

        while queue:
            row, col, steps = queue.popleft()
            if at_exit(row, col):
                if not ((row, col) == tuple(entrance)):
                    return steps

            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                if is_valid(nrow, ncol) and (nrow, ncol) not in state:
                    queue.append((nrow, ncol, steps+1))
                    state.add((nrow, ncol))

        return -1

