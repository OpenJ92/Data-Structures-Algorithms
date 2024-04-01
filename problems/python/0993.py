# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(None, root)])
        while queue:
            length = len(queue)
            for _ in range(length):
                parent, child = queue.popleft()
                if child.left:
                    queue.append((child, child.left))
                if child.right:
                    queue.append((child, child.right))

            cousin, cousjn = None, None
            for parent, child in queue:
                if child.val == x:
                    cousin = parent.val
                if child.val == y:
                    cousjn = parent.val
            if cousin and cousjn:
                return cousin != cousjn

        return False
