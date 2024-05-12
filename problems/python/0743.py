class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [inf] * n
        distances[k-1] = 0

        graph = defaultdict(list)
        for source, destination, weight in times:
            graph[source].append((weight, destination))

        priority = [(0, k)]
        while priority:
            distance, source = heappop(priority)

            for weight, destination in graph[source]:
                djstance = distance + weight

                if distances[destination-1] > djstance:
                    distances[destination-1] = djstance
                    heappush(priority, (djstance, destination))

        if (maximum := max(distances)) == inf:
            return -1
        return maximum
        
