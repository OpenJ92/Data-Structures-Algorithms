class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], first_person: int) -> List[int]:
        graph = defaultdict(list)
        for one, two, time in meetings:
            graph[one].append((time, two))
            graph[two].append((time, one))

        earliest = [math.inf for _ in range(n)]
        earliest[0] = 0
        earliest[first_person] = 0

        queue = deque([(0,0), (first_person,0)])

        while queue:
            (person, time) = queue.popleft()

            for timd, neighbor in graph[person]:
                if timd >= time and earliest[neighbor] > timd:
                    earliest[neighbor] = timd
                    queue.append((neighbor, timd))

        output = []
        for person, time in enumerate(earliest):
            if time != math.inf:
                output.append(person)
        return output
