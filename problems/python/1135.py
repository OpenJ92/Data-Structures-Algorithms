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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        priority = []
        for source, destination, cost in connections:
            heappush(priority, (cost, source, destination))

        disjoint = UnionFind()
        for city in range(1, n+1):
            disjoint.add(city)

        total, nodes = 0, n - 1
        while priority and nodes > 0:
            cost, source, destination = heappop(priority)
            if not disjoint.connected(source, destination):
                disjoint.union(source, destination)
                total += cost
                nodes -= 1

        if disjoint.groups > 1:
            return -1

        return total

