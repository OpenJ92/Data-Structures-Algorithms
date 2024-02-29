# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = lambda lst: all(x % 2 == 0 for x in lst)
        odd  = lambda lst: all(x % 2 != 0 for x in lst)
        increasing = lambda lst: all(i < j for i, j in zip(lst, lst[1:]))
        decreasing = lambda lst: all(i > j for i, j in zip(lst, lst[1:]))

        even_indexed = {'parity' : odd, 'change' : increasing}
        odd_indexed = {'parity' : even, 'change' : decreasing}
        functions = cycle([even_indexed, odd_indexed])

        def valid(level, functions):
            parity = functions['parity'](level)
            change = functions['change'](level)
            return parity and change

        queue = deque([root])
        level = [root.val]
        check = next(functions)

        while queue:
            if not valid(level, check):
                return False

            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)

            check = next(functions)

        return True
