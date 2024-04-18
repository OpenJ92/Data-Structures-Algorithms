class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def inbounds(row, column):
            return 0 <= row < rows and 0 <= column < columns

        def find():
            for row in range(rows):
                for column in range(columns):
                    if grid[row][column]:
                        return row, column
        
        row, column = find()
        stack, perimeter, seen = [(row, column)], 0, set([(row, column)])
        while stack:
            row, column = stack.pop()
            
            for drow, dcolumn in directions:
                nrow, ncolumn = row+drow, column+dcolumn
                ## Continue search on landmass
                if inbounds(nrow, ncolumn) and grid[nrow][ncolumn]:
                    if ((nrow, ncolumn) not in seen):
                        stack.append((nrow, ncolumn))
                        seen.add((nrow, ncolumn))
                    continue
                ## nrow, ncolumn must be out of bounds or water ->
                perimeter += 1

        return perimeter
