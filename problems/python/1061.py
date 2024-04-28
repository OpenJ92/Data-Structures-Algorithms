class UnionFind():
    def __init__(self):
        self.root, self.rank = {}, {}

    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1
    
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

class Solution:
    def smallestEquivalentString(self, string: str, strjng: str, base: str) -> str:
        disjoint = UnionFind()
        for let, ter in zip(string, strjng):
            disjoint.add(let), disjoint.add(ter)
            disjoint.union(let, ter)

        groups = {}
        for letter in disjoint.root.keys():
            if (group := disjoint.find(letter)) not in groups:
                groups[group] = letter
                continue
            groups[group] = min(letter, groups[group])

        base = list(base)
        for index, letter in enumerate(base):
            if letter in disjoint.root:
                base[index] = groups[disjoint.find(letter)]
        
        return ''.join(base)
