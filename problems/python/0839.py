class UnionFind():
    def __init__(self):
        self.root, self.rank, self.groups = {}, {}, 0

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

class Solution:
    def numSimilarGroups(self, strings: List[str]) -> int:

        def similar(string, strjng):
            count = 0
            for char, chbr in zip(string, strjng):
                count += char != chbr
                if count > 2:
                    return False
            return True

        disjoint, length = UnionFind(), len(strings)
        for index in range(length):
            disjoint.add(strings[index])

        for index in range(length):
            for jndex in range(index+1, length):
                if similar(strings[index], strings[jndex]):
                    disjoint.union(strings[index], strings[jndex])

        return disjoint.groups
