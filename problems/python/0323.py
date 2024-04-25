## https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)

        nodes = set(range(n))
        visited = set()
        components = 0

        while nodes:
            curr = nodes.pop()
            path = deque([curr])
            visited.add(curr)
            while path:
                node = path.pop()
                neighbors = graph[node]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        path.append(neighbor)
                        visited.add(neighbor)
                        nodes.remove(neighbor)
            components += 1
        return components

class UnionFind():
    def __init__(self):
        self.root, self.rank, self.count = {}, {}, 0
    
    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1
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

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint = UnionFind()

        for index in range(n):
            disjoint.add(index)

        for source, destination in edges:
            disjoint.union(source, destination)
        
        return disjoint.count

