# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def is_leaf(node):
          return not node.right and not node.left

        def dfs(node):
            if not node:
              return ""

            if node.left and node.right:
              return f"{node.val}({dfs(node.left)})({dfs(node.right)})"
            if node.left and not node.right:
              return f"{node.val}({dfs(node.left)})"
            if not node.left and node.right:
              return f"{node.val}()({dfs(node.right)})"
            if not node.left and not node.right:
              return f"{node.val}"

        return dfs(root)
