# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, internal_max):
            if not node:
                return 0, 0

            left,  lmax = dfs(node.left, internal_max)
            right, rmax = dfs(node.right, internal_max)
            internal_max = max(lmax, rmax, left + right)

            return 1 + max(left, right), internal_max

        left, lmax = dfs(root.left, 0)
        right, rmax = dfs(root.right, 0)
        return max(left + right, lmax, rmax)
