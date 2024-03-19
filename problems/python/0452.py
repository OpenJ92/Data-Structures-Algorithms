class Monotonic_TLE:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        def intersecting(interval, jnterval):
            start1, end1 = interval
            start2, end2 = jnterval
            return end2 >= start1 and start2 <= end1

        def intersect(interval, jnterval):
            lower, upper = interval
            lpwer, vpper = jnterval
            return max(lower, lpwer), min(upper, vpper)

        points.sort(key=lambda x: x[0])
        stack = []
        while points:
            point, *points = points

            if not stack:
               stack.append(point)
               continue

            while stack and intersecting(stack[-1], point):
                _point = stack.pop()
                point = intersect(point, _point)
            stack.append(point)

        return len(stack)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda point: point[1])
        rightmost, arrows = points[0][1], 1
        for left, right in points:
            if rightmost < left:
                rightmost = right
                arrows += 1
        return arrows
