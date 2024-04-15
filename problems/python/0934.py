class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def valid(row, column):
            return 0 <= row < rows and 0 <= column < columns

        def collect(row, column):
            stack, seen = [(row, column)],  set([(row, column)])
            while stack:
                row, column = stack.pop()

                for direction in directions:
                    drow, dcolumn = direction
                    nrow, ncolumn = row+drow, column+dcolumn

                    if valid(nrow, ncolumn) and (nrow, ncolumn) not in seen \
                                            and grid[nrow][ncolumn] == 1:
                        stack.append((nrow, ncolumn))
                        seen.add((nrow, ncolumn))

            return seen

        ## Collect nodes belonging to the first island encountered
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    collection = collect(row, column)
                    break

        queue = deque([(point, 0) for point in collection])
        while queue:
            length = len(queue)
            for _ in range(length):
                (row, column), bridge = queue.popleft()

                for direction in directions:
                    drow, dcolumn = direction
                    nrow, ncolumn = row+drow, column+dcolumn
                    
                    if valid(nrow, ncolumn) and (nrow, ncolumn) not in collection \
                                            and grid[nrow][ncolumn] == 1:
                        return bridge

                    if valid(nrow, ncolumn) and (nrow, ncolumn) not in collection: 
                        queue.append(((nrow, ncolumn), bridge + 1))
                        collection.add((nrow, ncolumn))
                        continue


        return -1
