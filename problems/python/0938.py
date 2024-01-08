# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inside(value):
            return low <= value <= high

        def dfs(node, accum):
            if not node:
                return accum

            if inside(node.val):
                accum += node.val

            left = dfs(node.left, accum)
            right = dfs(node.right, left)
            return right

        return dfs(root, 0
