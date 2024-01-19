class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        def slope(point_one, point_two):
            x, y = point_one
            u, v = point_two

            numerator   = y - v
            denominator = x - u

            if not denominator:
                return math.inf
            return numerator / denominator

        root, *coordinates, tail = coordinates
        control = slope(root, tail)

        for coordinate in coordinates:
            if slope(root, coordinate) != control:
                return False
        return True

