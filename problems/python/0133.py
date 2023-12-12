from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        stack = deque([node])
        memo = {node : Node(node.val, [])}
        while stack:
            nnode = stack.pop()
            for neighbor in nnode.neighbors:
                if neighbor not in memo:
                    memo[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                memo[nnode].neighbors.append(memo[neighbor])

        return memo[node]

