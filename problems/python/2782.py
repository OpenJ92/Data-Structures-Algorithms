class UnionFind():
    def __init__(self):
        self.root, self.rank, self.groups = {}, {}, 0

    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1
            self.groups += 1

    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node, npde):
        root = self.find(node)
        rppt = self.find(npde)

        if root != rppt:
            if self.rank[root] > self.rank[rppt]:
                self.root[rppt] = root
            if self.rank[root] > self.rank[rppt]:
                self.root[root] = rppt
            else:
                self.root[rppt] = root
                self.rank[rppt] += 1
            self.groups -= 1

# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, category_handler: Optional['CategoryHandler']) -> int:
        disjoint = UnionFind()
        for index in range(n):
            disjoint.add(index)

        for index in range(n):
            for jndex in range(index+1, n):
                if category_handler.haveSameCategory(index, jndex):
                    disjoint.union(index, jndex)

        return disjoint.groups
