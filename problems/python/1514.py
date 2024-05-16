class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], probability: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for index, (source, destination) in enumerate(edges):
            graph[source].append((probability[index], destination))
            graph[destination].append((probability[index], source))

        maximums = [0 for _ in range(n)]
        maximums[start] = 1

        priority = [(-maximums[start], start)]
        while priority:
            path, source = heappop(priority)

            if source == end:
                return -path

            for prob, destination in graph[source]:
                if -path * prob > maximums[destination]:
                    maximums[destination] = -path * prob
                    heappush(priority, (-maximums[destination], destination))

        return 0
        
