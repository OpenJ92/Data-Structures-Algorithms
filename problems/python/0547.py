class UnionFind():
    def __init__(self):
        self.root, self.rank = {}, {}
        self.count = 0

    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1
            self.count += 1

    def union(self, node, npde):
        root = self.find(node)
        rppt = self.find(npde)

        if root != rppt:
            if self.rank[root] > self.rank[rppt]:
                self.root[rppt] = root
            if self.rank[root] < self.rank[rppt]:
                self.root[root] = rppt
            else:
                self.root[root] = rppt
                self.rank[root] += 1

            self.count -= 1

    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

class Solution:
    def findCircleNum(self, connected: List[List[int]]) -> int:
        disjoint, rows, columns = UnionFind(), len(connected), len(connected[0])
        for row in range(rows):
            for column in range(columns):
                if connected[row][column] == 1:
                    disjoint.add(row)
                    disjoint.add(column)
                    disjoint.union(row, column)
        return disjoint.count
