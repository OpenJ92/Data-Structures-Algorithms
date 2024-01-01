# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Iterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque([(p, q)])

        while stack:
            p, q = stack.pop()

            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Recursive:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            this_subtree = left.val == right.val
            left_subtree = dfs(left.left, right.left)
            right_subtree = dfs(left.right, right.right)

            return this_subtree and left_subtree and right_subtree

        return dfs(p, q)
