class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows    = len(grid)
        self.columns = len(grid[0])
        self.LAND  = 1
        self.WATER = 0
        self.DIRECTIONS = [(0,1), (1,0), (0,-1), (-1, 0)]

        visited = set()
        queue = deque()

        max_island_area = -math.inf
        for location in product(range(self.rows), range(self.columns)):
            if self.access(grid, *location) == self.LAND and location not in visited:
                queue.append(location)
                visited.add(location)
                island_area = self.measure_island_area(queue, visited, grid)
                max_island_area = max(island_area, max_island_area)
        return max_island_area if max_island_area != -math.inf else 0

    def measure_island_area(self, queue, visited, grid):
        island_area = 0
        while queue:
            location = queue.pop()
            island_area += 1

            for direction in self.DIRECTIONS:
                new_location = self.update_location(location, direction)
                if self.is_valid(new_location, grid, visited):
                    queue.append(new_location)
                    visited.add(new_location)

        return island_area

    def is_valid(self, location, grid, visited) -> bool:
        if self.is_inbounds(location) \
                and self.access(grid, *location) == self.LAND \
                and location not in visited:
            return True
        return False

    def is_inbounds(self, location):
        x, y = location
        if 0 <= x < self.rows and 0 <= y < self.columns:
            return True
        return False

    def update_location(self, location: List[int], direction: List[int]) -> List[int]:
        return tuple(x + y for x, y in zip(location, direction))

    def access(self, grid, row, col):
        return grid[row][col]
