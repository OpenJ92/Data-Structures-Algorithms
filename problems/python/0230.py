# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = k
        val = -1

        def dfs(node):
            if not node:
                return

            left = dfs(node.left)
            nonlocal kth, val; kth -= 1
            if kth == 0:
                val = node.val
                return
            elif kth <= 0:
                return
            right = dfs(node.right)

        dfs(root)
        return val
