class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse = defaultdict(list)
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse[neighbor].append(node)

        safe = [False] * len(graph)
        indegree = [0] * len(graph)
        for node, neighbors in enumerate(graph):
            indegree[node] = len(neighbors)

        queue = deque([])
        for node in range(len(graph)):
            if not indegree[node]:
                queue.append(node)

        while queue:
            node = queue.popleft()
            safe[node] = True

            for neighbor in reverse[node]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)
        
        output = []
        for node in range(len(graph)):
            if safe[node]:
                output.append(node)

        return output
