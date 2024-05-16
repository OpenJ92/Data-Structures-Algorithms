class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        functions = { 2:lambda x, y: x or y
                    , 3:lambda x, y: x and y
                    }

        def leaf(node):
            return not node.left and not node.right

        def dfs(node):
            if leaf(node):
                return node.val

            return functions[node.val](dfs(node.left), dfs(node.right))

        return dfs(root)

