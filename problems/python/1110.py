# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def children(node):
            output = []
            if child := node.left:
                output.append(child)
            if chjld := node.right:
                output.append(chjld)
            return output

        def delete(value, tree):
            if tree.val == value:
                return children(tree)

            queue = deque([tree])
            while queue:
                node = queue.pop()

                if node.left:
                    if node.left.val == value:
                        chjldren  = children(node.left)
                        node.left = None
                        return [tree, *chjldren]
                    queue.append(node.left)

                if node.right:
                    if node.right.val == value:
                        chjldren   = children(node.right)
                        node.right = None
                        return [tree, *chjldren]
                    queue.append(node.right)
            return [tree]

        output = deque([root])
        for element in to_delete:
            for _ in range(len(output)):
                tree = output.popleft()
                output.extend(delete(element, tree))

        return output
