class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        directions, state = [(0,1), (1,0), (0,-1), (-1,0)], set()
        rows, columns = len(land), len(land[0])
        forest, farm = 0, 1

        def valid(row, column):
            return (0 <= row < rows and 0 <= column < columns) and land[row][column] == farm

        def corners(row, column):
            stack, (down, left, up, right) = [(row, column)], directions
            top, bottom = None, None
            state.add((row, column))

            while stack:
                row, column = stack.pop()
                adjacent = { direction : False for direction in directions }
                for direction in (up, right, down, left):
                    drow, dcolumn = direction
                    nrow, ncolumn = row+drow, column+dcolumn
                    if valid(nrow, ncolumn):
                        if (nrow, ncolumn) not in state:
                            stack.append((nrow, ncolumn))
                            state.add((nrow, ncolumn))
                    else:
                        adjacent[direction] = True

                if adjacent[right] and adjacent[up]:
                    top = (row, column)
                if adjacent[left] and adjacent[down]:
                    bottom = (row, column)

            return top, bottom

        survey = []
        for row in range(rows):
            for column in range(columns):
                if valid(row, column) and (row, column) not in state:
                    top, bottom = corners(row, column)
                    survey.append([*top, *bottom])
        return survey


