# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def check_elements(lst, check):
            for element in lst:
                if not check(element.val):
                    return False
            return True
        even = lambda lst: check_elements(lst, lambda x: x % 2 == 0)
        odd  = lambda lst: check_elements(lst, lambda x: x % 2 != 0)

        def compare_neighbors(lst, compare):
            length = len(lst)
            for index in range(1, length):
                if not compare(lst[index-1].val,lst[index].val):
                    return False
            return True
        increasing = lambda lst: compare_neighbors(lst, lambda x, y: x < y)
        decreasing = lambda lst: compare_neighbors(lst, lambda x, y: x > y)

        even_indexed = {'parity' : odd,  'change' : increasing}
        odd_indexed  = {'parity' : even, 'change' : decreasing}
        functions = cycle([even_indexed, odd_indexed])

        def valid(level, functions):
            parity = functions['parity'](level)
            change = functions['change'](level)
            return parity and change

        queue = deque([root])
        while queue:
            check = next(functions)
            if not valid(queue, check):
                return False

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return True

