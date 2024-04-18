class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        lonely = []
        def dfs(node):
            if not node:
                return

            if node.left and node.right:
                dfs(node.left)
                dfs(node.right)
                return

            nonlocal lonely
            if node.left and not node.right:
                lonely.append(node.left.val)
                dfs(node.left)
            if node.right and not node.left:
                lonely.append(node.right.val)
                dfs(node.right)

        dfs(root)
        return lonely
