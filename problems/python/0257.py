# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if not node.left and not node.right:
                paths.append("->".join(path[:]))
                return

            if node.left:
                path.append(str(node.left.val))
                dfs(node.left, path)
                path.pop()

            if node.right:
                path.append(str(node.right.val))
                dfs(node.right, path)
                path.pop()

        dfs(root, [str(root.val)])
        return paths

