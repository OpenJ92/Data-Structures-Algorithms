class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        columns = len(rooms[0])

        WALL = -1
        GATE = 0
        EMPTY = 2147483647

        MOVES = [(1,0), (0,1), (-1,0), (0,-1)]

        queue = deque([])
        state = set()
        for row, col in product(range(rows), range(columns)):
            if rooms[row][col] == GATE:
                queue.append((row, col, 0))
                state.add((row, col))

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < columns and rooms[row][col] == EMPTY

        while queue:
            row, col, steps = queue.popleft()
            for drow, dcol in MOVES:
                nrow, ncol = row + drow, col + dcol
                if valid(nrow, ncol) and (nrow, ncol) not in state:
                    queue.append((nrow, ncol, steps+1))
                    state.add((nrow, ncol))
                    rooms[nrow][ncol] = steps + 1

        return rooms

