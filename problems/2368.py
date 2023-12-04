class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        if 0 in restricted:
            return 0

        graph = defaultdict(list)
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)

        seen = set([0, *restricted])
        stack = deque([0])
        count = 1

        while stack:
            node = stack.pop()
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)
                    count += 1
        return count
