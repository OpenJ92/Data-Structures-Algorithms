class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        directional_graph = defaultdict(list)
        graph = defaultdict(list)

        for source, destination in connections:
            directional_graph[source].append(destination)
            graph[source].append(destination)
            graph[destination].append(source)

        count = 0
        stack = [0]
        state = set([0])
        while stack:
            node = stack.pop()
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in state:
                    if node not in directional_graph[neighbor]:
                        count += 1
                    stack.append(neighbor)
                    state.add(neighbor)

        return count
