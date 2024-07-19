class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def leaf(node):
            return not node.left and not node.right

        def postorder(node, total):
            if not node:
                return Counter(), 0
            if leaf(node):
                return Counter([node.val]), 0

            left,  ltotal = postorder(node.left, total)
            right, rtotal = postorder(node.right, total)

            total = ltotal + rtotal
            for _, count in left.items():
                for _, cpunt in right.items():
                    if count + cpunt <= distance:
                        total += 1

            for npde in left:
                left[npde] += 1
            for nqde in right:
                right[nqde] += 1

            return left | right, total

        _, total = postorder(root, 0)
        return total
