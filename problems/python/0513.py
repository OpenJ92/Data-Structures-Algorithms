class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            level = deque([])

            for element in range(len(queue)):
                node = queue[element]

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            if not level:
                return queue.popleft().val

            queue = level
