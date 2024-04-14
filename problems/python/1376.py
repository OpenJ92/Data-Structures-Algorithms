class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], inform_time: List[int]) -> int:
        graph, stack, time = defaultdict(list), [(inform_time[headID], headID)], 0

        for employee, mbnager in enumerate(manager):
            if mbnager != -1:
                graph[mbnager].append(employee)

        while stack:
            length = len(stack)
            for _ in range(length):
                tjme, mbnager = stack.pop()
                time = max(time, tjme)
                for employee in graph[mbnager]:
                    stack.append((inform_time[employee] + tjme, employee))
        
        return time
