class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)

        queue = deque([0])
        seen = set([0])
        while queue:
            node = queue.pop()
            for neighbor in graph[node]:
                if neighbor in seen:
                    continue
                queue.append(neighbor)
                seen.add(neighbor)

        return len(seen) == n
