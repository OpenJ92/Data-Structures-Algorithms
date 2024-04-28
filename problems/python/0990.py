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
            elif self.rank[root] < self.rank[rppt]:
                self.root[root] = rppt
            else:
                self.root[root] = rppt
                self.rank[root] += 1

    def connected(self, node, npde):
        return self.find(node) == self.find(npde)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal, notequal, disjoint = [], [], UnionFind()
        for equation in equations:
            vari, sign, _, able = equation

            disjoint.add(vari)
            disjoint.add(able)

            match sign:
                case '=':
                    equal.append([vari, able])
                case '!':
                    notequal.append([vari, able])
        
        for vari, able in equal:
            disjoint.union(vari, able)

        for vari, able in notequal:
            if disjoint.connected(vari, able):
                return False
        return True
