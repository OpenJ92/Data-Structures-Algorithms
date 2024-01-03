class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        queue = deque([])
        for row in bank:
            devices = row.count('1')
            if devices:
                queue.append(devices)
        if not queue:
            return 0

        first = queue.popleft()
        lasers = 0
        while queue:
            second = queue.popleft()
            lasers += first*second
            first = second

        return lasers
