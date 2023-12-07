class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED  = 0
        BLUE = 1

        graph = defaultdict(lambda: defaultdict(list))
        for source, destination in redEdges:
            graph[RED][source].append(destination)
        for source, destination in blueEdges:
            graph[BLUE][source].append(destination)

        queue = deque([(0, BLUE, 0), (0, RED, 0)])
        shortest_paths = [math.inf] * n
        seen = set([(0, BLUE), (0, RED)])

        while queue:
            node, color, steps = queue.popleft()
            shortest_paths[node] = min(steps, shortest_paths[node])
            neighbors = graph[color][node]
            for neighbor in neighbors:
                if (neighbor, 1 - color) not in seen:
                    queue.append((neighbor, 1 - color, steps + 1))
                    seen.add((neighbor, 1 - color))

        return [short if short!=math.inf else -1 for short in shortest_paths]

