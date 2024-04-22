class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        make, queue = lambda lock: tuple(map(int, lock)), deque([((0,0,0,0), 0)])
        target, seen = make(target), set(map(make, deadends))

        if (0, 0, 0, 0) in seen:
            return -1

        def construct(node, increment, index):
            nnode = []
            for jndex in range(len(node)):
                element = (node[jndex] + (increment * (index==jndex))) % 10
                nnode.append(element)
            return tuple(nnode)

        while queue:
            length = len(queue)
            for neighbor in range(len(queue)):
                node, steps = queue.popleft()

                if node == target:
                    return steps

                for index, increment in product(range(4), [-1, 1]):
                    nnode = construct(node, increment, index)
                    if nnode not in seen:
                        queue.append((nnode, steps+1))
                        seen.add(nnode)

        return -1

