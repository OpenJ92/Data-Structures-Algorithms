# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        stack = deque([(root, False)])
        cache = {}
        cache[None] = (0, 0)
        result = 0

        ## Iter - Backtracking w/t cache. @tyler-liu
        while stack:
            node, seen = stack.pop()

            if node is None:
                continue
            if not seen:
                stack.extend([ (node      , True )
                             , (node.left , False)
                             , (node.right, False)
                             ])
            else:
                summation = node.val + cache[node.left][0] + cache[node.right][0]
                count = 1 + cache[node.left][1] + cache[node.right][1]
                if summation // count == node.val:
                    result += 1
                cache[node] = (summation, count)

        return result
