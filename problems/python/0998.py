class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        characters = {}
        for index, character in enumerate('abcdefghijklmnopqrstuvwxyz'):
            characters[index] = character

        def leaf(node):
            return not node.right and not node.left

        minimum = ""
        def dfs(node, string):
            nonlocal minimum
            this = characters[node.val]

            if leaf(node):
                if not minimum or minimum > this + string:
                    minimum = this + string
            if node.left:  
                dfs(node.left, this + string)
            if node.right: 
                dfs(node.right, this + string)

        dfs(root, "")
        return minimum
