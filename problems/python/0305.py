class UnionFind():
    def __init__(self):
        self.root = {}
        self.rank = {}
        self.count = 0

    def add(self, node):
        if node not in self.root:
            self.root[node], self.rank[node] = node, 1
            self.count += 1

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node, npde):
        rnode = self.find(node)
        rnpde = self.find(npde)

        if rnode != rnpde:
            if self.rank[rnode] > self.rank[rnpde]:
                self.root[rnpde] = rnode
            if self.rank[rnode] < self.rank[rnpde]:
                self.root[rnode] = rnpde
            else:
                self.root[rnode] = rnpde
                self.rank[rnode] += 1

            self.count -= 1

    def connected(self, node, npde):
        return self.find(node) == self.find(npde)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        disjoint, directions = UnionFind(), [(0,1),(1,0),(0,-1),(-1,0)]

        def valid(row, column):
            return 0 <= row < m and 0 <= column < n and (row, column) in disjoint.root

        output = []
        for row, column in positions:
            disjoint.add((row, column))

            for drow, dcolumn in directions:
                nrow, ncolumn = row+drow, column+dcolumn
                if valid(nrow, ncolumn):
                    disjoint.union((row, column), (nrow, ncolumn))

            output.append(disjoint.count)

        return output
