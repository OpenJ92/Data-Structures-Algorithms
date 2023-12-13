class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return sqrt(x**2 + y**2)

        prioritized = []
        for point in points:
            prioritized.append((dist(*point), point))

        heapify(prioritized)
        k_closest = []
        while k:
            _, point = heappop(prioritized)
            k_closest.append(point)
            k -= 1

        return k_closest
