# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def backtrack(node):
            if not node: return 0

            take = node.val
            skip = backtrack(node.left) + backtrack(node.right)
            if node.left:
                take += backtrack(node.left.left) + backtrack(node.left.right)
            if node.right:
                take += backtrack(node.right.left) + backtrack(node.right.right)

            return max(skip, take)

        return backtrack(root)
