class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        grid = tuple(map(tuple, grid))
        space = list(product(product(range(3), range(3)), [(1,0),(0,-1),(-1,0),(0,1)]))
        target = ((1,1,1),(1,1,1),(1,1,1))

        def valid(row, column):
            return 0 <= row < 3 and 0 <= column < 3

        def construct(node, row, col, nrow, ncol):
            nnode = [[0 for _ in range(3)] for _ in range(3)]
            for (trow, tcol) in product(range(3), range(3)):
                nnode[trow][tcol] = node[trow][tcol]
            nnode[row][col]   -= 1
            nnode[nrow][ncol] += 1
            return tuple(map(tuple, nnode))

        queue = deque([(0, grid)])
        state = set([grid])

        while queue:
            steps, node = queue.popleft()
            if node == target:
                return steps

            for (row, col), (drow, dcol) in space:
                nrow, ncol = row+drow, col+dcol
                if not valid(nrow, ncol):
                    continue

                if not node[nrow][ncol]:
                    nnode = construct(node, row, col, nrow, ncol)
                    if nnode not in state:
                        queue.append((steps+1, nnode))
                        state.add(nnode)
