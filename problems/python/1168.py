class UnionFind():
    def __init__(self):
        self.root, self.rank, self.count = {}, {}, 0
    
    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 0
            self.count += 1
        
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
            self.count -= 1
    
    def connected(self, node, npde):
        return self.find(node) == self.find(npde)

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        for index in range(len(pipes)):
            house, hpuse, cost = pipes[index]
            pipes[index] = tuple((cost, house, hpuse))

        for house, well in enumerate(wells):
            pipes.append((well, house + 1, 0))
        heapify(pipes)

        disjoint = UnionFind()
        for house in range(n+1):
            disjoint.add(house)

        houses, minimum = n + 1, 0
        while pipes and houses > 0:
            cost, house, hpuse = heappop(pipes)
            if not disjoint.connected(house, hpuse):
                disjoint.union(house, hpuse)
                minimum += cost
                houses -= 1

        if disjoint.count > 1:
            return -1

        return minimum
