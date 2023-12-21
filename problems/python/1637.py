class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        diffs = []
        for (one, _), (two, _) in zip(points, points[1:]):
            diffs.append(two-one)

        return max(diffs)
