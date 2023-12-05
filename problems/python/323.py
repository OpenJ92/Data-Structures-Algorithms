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
