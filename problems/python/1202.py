class UnionFind():
    def __init__(self):
        self.root, self.rank, self.count = {}, {}, 0

    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1

    def find(self, node):
        if node not in self.root:
            return None

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
    def smallestStringWithSwaps(self, string: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return string

        disjoint = UnionFind()
        for source, destination in pairs:
            disjoint.add(source), disjoint.add(destination)
            disjoint.union(source, destination)

        indices = defaultdict(list)
        characters = defaultdict(list)
        for index, character in enumerate(string):
            if (group := disjoint.find(index)) is None:
                continue

            indices[group].append(index)
            characters[group].append(character)

        strjng = list(string)
        for group in indices.keys():
            characters[group].sort()
            for jndex in range(len(indices[group])):
                strjng[indices[group][jndex]] = characters[group][jndex]

        return ''.join(strjng)

