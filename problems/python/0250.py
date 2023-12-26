class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return True, None
            if not node.left and not node.right:
                count += 1
                return True, node.val

            univalue_left,  left = dfs(node.left)
            univalue_right, right = dfs(node.right)
            univalue_curr = len(set(filter(lambda val: val != None, [left, right, node.val]))) == 1

            if univalue_curr and univalue_left and univalue_right:
                count += 1

            return univalue_curr and univalue_left and univalue_right, node.val

        dfs(root)
        return count
