# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(nodes):
            if not nodes:
                return None

            mid  = (len(nodes)) // 2
            node = nodes[mid]

            left  = nodes[:mid]
            right = nodes[mid+1:]

            return TreeNode(val = node, left = construct(left), right = construct(right))

        return construct(nums)

