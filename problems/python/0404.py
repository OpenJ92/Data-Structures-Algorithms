# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def leaf(node):
            if not node.left and not node.right:
                return True
            return False

        stack, total = [root], 0
        while stack:
            node = stack.pop()

            if node.left and leaf(node.left):
                total += node.left.val
            elif node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)
                
        return total
