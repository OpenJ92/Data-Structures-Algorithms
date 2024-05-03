class UnionFind():
    def __init__(self):
        self.root = {}
        self.rank = {}
        self.groups = 0

    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1
            self.groups += 1

    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node, npde):
        root = self.find(node)
        rppt = self.find(npde)

        if root != rppt:
            if self.rank[root] > self.rank[rppt]:
                self.root[rppt] = root
            elif self.rank[root] < self.rank[rppt]:
                self.root[root] = rppt
            else:
                self.root[root] = rppt
                self.rank[root] += 1
            self.groups -= 1

    def connected(self, node, npde):
        return self.find(node) == self.find(npde)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(point, pojnt):
            x, y = point
            u, v = pojnt
            return abs(x - u) + abs(y - v)

        disjoint, priority, length = UnionFind(), [], len(points)
        for index in range(length):
            for jndex in range(index+1, length):
                dist = manhattan(points[index], points[jndex])
                point, pojnt = tuple(points[index]), tuple(points[jndex])
                disjoint.add(point), disjoint.add(pojnt)
                heappush(priority, (dist, point, pojnt))

        nodes, minimum = disjoint.groups - 1, 0
        while priority and nodes > 0:
            dist, point, pojnt = heappop(priority)
            if not disjoint.connected(point, pojnt):
                disjoint.union(point, pojnt)
                minimum += dist
                nodes -= 1

        return minimum

