# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        characters = {}
        for index, character in enumerate('abcdefghijklmnopqrstuvwxyz'):
            characters[index] = character

        def leaf(node):
            return not node.right and not node.left

        stack, minimum = [(root, "")], ""
        while stack:
            node, string = stack.pop()
            this = characters[node.val]

            if leaf(node) and (not minimum or minimum > this + string):
                minimum = this + string
                continue

            if node.left:
                stack.append((node.left, this + string))
            if node.right:
                stack.append((node.right, this + string))

        return minimum
