# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def path(node, value, directions):
            if not node:
                return False

            if node.val == value:
                return True

            directions.append("L")
            if path(node.left, value, directions):
                return True
            directions.pop()

            directions.append("R")
            if path(node.right, value, directions):
                return True
            directions.pop()

        start, destination = [], []
        path(root, startValue, start), path(root, destValue, destination)

        index, upper = 0, min(len(start), len(destination))
        while index < upper and start[index] == destination[index]:
            index += 1

        return "".join(["U"] * (len(start) - index) + destination[index:])
