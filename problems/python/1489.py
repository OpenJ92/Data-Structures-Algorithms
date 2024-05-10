class UnionFind():
    def __init__(self, n):
        self.root, self.rank, self.components = {}, {}, n
        for node in range(n):
            self.root[node] = node
            self.rank[node] = 1

    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1
            self.components += 1

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
            elif self.rank[rppt] > self.rank[root]:
                self.root[root] = rppt
            else:
                self.root[root] = rppt
                self.rank[root] += 1
            self.components -= 1

    def connected(self, node, npde):
        return self.find(node) == self.find(npde)

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def kruskal(edges, disjoint, ignore, weight):
            for index, edge in edges:
                if edge == ignore:
                    continue

                a, b, cost = edge
                if not disjoint.connected(a, b):
                    disjoint.union(a, b)
                    weight += cost
                    nodes -= 1

            if disjoint.components == 1:
                return weight
            return None

        for index in range(len(edges)):
            edges[index] = (index, edges[index])

        disjoint, _ = UnionFind(n), edges.sort(key=lambda x: x[1][2])
        base = kruskal(edges, disjoint, None, 0)

        critical, psudocritical = set(), set()
        for index, (a, b, cost) in edges:
            disjoint, djsjoint = UnionFind(n), UnionFind(n)
            djsjoint.union(a, b)

            ignore = kruskal(edges, disjoint, [a, b, cost], 0)
            if ignore is None or ignore > base:
                critical.add(index)
                continue

            forced = kruskal(edges, djsjoint, None, cost)
            if forced == base:
                psudocritical.add(index)

        return [critical, psudocritical]

