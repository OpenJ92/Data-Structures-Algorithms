## https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = set()
        path = deque([source])

        while path:
            node = path.pop()
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
        return False

